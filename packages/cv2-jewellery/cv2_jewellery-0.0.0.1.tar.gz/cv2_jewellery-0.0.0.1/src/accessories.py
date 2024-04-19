import cv2
from utils import low_pass_filter
import numpy as np

earring_img = cv2.imread('data/jewellery/default/earring.png',-1)
flipped_earring_img = cv2.flip(earring_img, 1)  # Flip the earring image for the right ear
nose_ring_img = cv2.imread('data/jewellery/default/nose-ring.png', -1)
necklace_img = cv2.imread('data/jewellery/default/Necklace.png', -1) 

def overlay_image(frame, image, position, scale_factor):
    h, w = image.shape[:2]
    scaled_h, scaled_w = int(h * scale_factor), int(w * scale_factor)
    scaled_image = cv2.resize(image, (scaled_w, scaled_h))

    x, y = int(position[0] - scaled_w / 2), int(position[1] - scaled_h / 2) + 30
    
    if x < 0 or y < 0 or x + scaled_w > frame.shape[1] or y + scaled_h > frame.shape[0]:
        return frame
    
    alpha_s = scaled_image[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(3):
        frame[y:y+scaled_h, x:x+scaled_w, c] = (alpha_s * scaled_image[:, :, c] +
                                                 alpha_l * frame[y:y+scaled_h, x:x+scaled_w, c])
    
    return frame

# Function to overlay earrings on the frame at smoothed ear positions
def overlay_earrings(frame, poses, earring_scale_factor=0.2, alpha=0):
    # Initialize previous positions
    global earring_img, flipped_earring_img
    prev_left_ear = None
    prev_right_ear = None
    
    left_ear_detected = False
    right_ear_detected = False
    
    for pose in poses:
        left_ear = pose.keypoints.get(3)  # Index of left ear
        right_ear = pose.keypoints.get(4)  # Index of right ear
        
        if left_ear is not None:
            left_ear_position = left_ear.position
            # Apply low-pass filter to smooth the left ear position
            left_ear_smoothed = low_pass_filter((left_ear_position.x, left_ear_position.y), prev_left_ear, alpha)
            # Overlay left earring image at smoothed left ear position
            frame = overlay_image(frame, earring_img, left_ear_smoothed, earring_scale_factor)
            prev_left_ear = left_ear_smoothed  # Update previous position
            left_ear_detected = True
        
        if right_ear is not None:
            right_ear_position = right_ear.position
            # Apply low-pass filter to smooth the right ear position
            right_ear_smoothed = low_pass_filter((right_ear_position.x, right_ear_position.y), prev_right_ear, alpha)
            # Overlay flipped earring image at smoothed right ear position
            frame = overlay_image(frame, flipped_earring_img, right_ear_smoothed, earring_scale_factor)
            prev_right_ear = right_ear_smoothed  # Update previous position
            right_ear_detected = True
    
    # If either left or right ear is not detected, clear the overlay
    if not (left_ear_detected and right_ear_detected):
        frame = np.zeros_like(frame)
    
    return frame

# Function to overlay nose ring on the frame
def overlay_nose_ring(frame, nose_ring_point):
    global nose_ring_img
    if nose_ring_img is not None:
        # Resize the ring image with scale factor
        nose_ring_height, nose_ring_width, _ = nose_ring_img.shape
        scale_factor = 0.1  # Adjust scale as needed to increase or decrease size
        nose_ring_img_resized = cv2.resize(nose_ring_img, (int(nose_ring_width * scale_factor), int(nose_ring_height * scale_factor)))

        # Calculate the top-left corner coordinates for placing the nose ring
        x_offset = int(nose_ring_point[0] - nose_ring_img_resized.shape[1] / 2)  # Adjust x coordinate
        y_offset = int(nose_ring_point[1] - nose_ring_img_resized.shape[0] / 2)  # Adjust y coordinate

        # Check if the nose ring image is within the bounds of the frame
        if x_offset >= 0 and y_offset >= 0 and x_offset + nose_ring_img_resized.shape[1] <= frame.shape[1] and y_offset + nose_ring_img_resized.shape[0] <= frame.shape[0]:
            # Overlay the nose ring image on the frame
            for c in range(3):
                frame[y_offset:y_offset+nose_ring_img_resized.shape[0], x_offset:x_offset+nose_ring_img_resized.shape[1], c] = \
                    nose_ring_img_resized[:,:,c] * (nose_ring_img_resized[:,:,3] / 255.0) + \
                    frame[y_offset:y_offset+nose_ring_img_resized.shape[0], x_offset:x_offset+nose_ring_img_resized.shape[1], c] * (1.0 - nose_ring_img_resized[:,:,3] / 255.0)
    return frame

# Function to overlay necklace on the frame
def overlay_necklace(frame, left_shoulder, right_shoulder):
    global necklace_img
    # Calculate the center point between left and right shoulders
    neck_center_x = int((left_shoulder.x + right_shoulder.x) * frame.shape[1] / 2)
    neck_center_y = int((left_shoulder.y + right_shoulder.y) * frame.shape[0] / 2)

    # Overlay the necklace image on the frame
    if necklace_img is not None:
        # Resize the necklace image with scale factor
        necklace_height, necklace_width, _ = necklace_img.shape
        scale_factor = 0.18  # Adjust scale as needed to increase or decrease size
        necklace_img_resized = cv2.resize(necklace_img, (int(necklace_width * scale_factor), int(necklace_height * scale_factor)))

        # Calculate the top-left corner coordinates for placing the necklace
        x_offset = int(neck_center_x - necklace_img_resized.shape[1] / 2)  # Adjust x coordinate
        y_offset = int(neck_center_y - necklace_img_resized.shape[0] / 2) - 10 # Adjust y coordinate

        # Check if the necklace image is within the bounds of the frame
        if x_offset >= 0 and y_offset >= 0 and x_offset + necklace_img_resized.shape[1] <= frame.shape[1] and y_offset + necklace_img_resized.shape[0] <= frame.shape[0]:
            # Overlay the necklace image on the frame
            for c in range(3):
                frame[y_offset:y_offset+necklace_img_resized.shape[0], x_offset:x_offset+necklace_img_resized.shape[1], c] = \
                    necklace_img_resized[:,:,c] * (necklace_img_resized[:,:,3] / 255.0) + \
                    frame[y_offset:y_offset+necklace_img_resized.shape[0], x_offset:x_offset+necklace_img_resized.shape[1], c] * (1.0 - necklace_img_resized[:,:,3] / 255.0)
    return frame