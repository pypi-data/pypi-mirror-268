import mode
class cv2_jewellery:
    def __init__(self, mode='image', assets='all', scale_factor=[0.1, 0.1, 0.1], height=[0, 0, 0]):
        self.mode = mode
        self.assets = assets
        self.scale_factor = scale_factor
        self.height = height
        
    def apply(self):
        mode.display_webcam()
        

def main():
    data = cv2_jewellery()
    data.apply()


if __name__ == "__main__":
    main()

# cv2_jewellery(mode=video,assets =[earring,nose_ring,neckless],scale_factor = [0.2,0.3,0.2],height=[10,20,10])