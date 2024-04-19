import mediapipe as mp
from tf_bodypix.api import download_model, load_model, BodyPixModelPaths
from accessories import overlay_image, cv2, np, overlay_earrings,overlay_necklace,overlay_nose_ring


# Load the bodypix model
bodypix_model = load_model(download_model(BodyPixModelPaths.MOBILENET_FLOAT_100_STRIDE_16))

def display_webcam(input_path=None):
    resize_width, resize_height = 640, 480

    if input_path:
        cap = cv2.VideoCapture(input_path)
    else:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, resize_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resize_height)

    # Initialize MediaPipe face mesh and pose models
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)  # Flip the frame if needed

        # Detect face mesh landmarks
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_frame)

        # Detect pose landmarks
        pose_result = pose.process(rgb_frame)

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                # Get landmark coordinates for the nose ring (index 439)
                nose_ring_point = (int(face_landmarks.landmark[439].x * frame.shape[1]),
                                   int(face_landmarks.landmark[439].y * frame.shape[0]))
                frame = overlay_nose_ring(frame, nose_ring_point)

        if pose_result.pose_landmarks:
            left_shoulder = pose_result.pose_landmarks.landmark[11]
            right_shoulder = pose_result.pose_landmarks.landmark[12]
            frame = overlay_necklace(frame, left_shoulder, right_shoulder)

        # Run BodyPix to get poses
        result = bodypix_model.predict_single(frame)
        poses = result.get_poses()

        frame_with_earrings = overlay_earrings(frame, poses, earring_scale_factor=0.05)
        cv2.imshow('Webcam with Overlays', frame_with_earrings)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def capture_image(output_img_path, input_path=None):
    if input_path:
        frame = cv2.imread(input_path)
    else:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            return
        cap.release()

    cv2.imwrite(output_img_path, frame)
    print("Image captured successfully!")

def capture_video(output_video_path, capture_duration=10, input_path=None):
    if input_path:
        cap = cv2.VideoCapture(input_path)
    else:
        cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (640, 480))

    start_time = cv2.getTickCount()
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < capture_duration:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video.")
            break
        out.write(frame)

    cap.release()
    out.release()
