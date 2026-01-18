import cv2
import numpy as np

def enhance_contrast(gray_image):
    min_val = np.min(gray_image)
    max_val = np.max(gray_image)

    if max_val - min_val == 0:
        return gray_image

    stretched = (gray_image - min_val) * (255 / (max_val - min_val))
    return stretched.astype(np.uint8)
