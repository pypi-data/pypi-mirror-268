import numpy as np

# Define a simple low-pass filter function
def low_pass_filter(current_position, previous_position, alpha):
    if previous_position is None:
        return current_position
    else:
        return tuple(alpha * np.array(current_position) + (1 - alpha) * np.array(previous_position))