import cv2

def reduce_noise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)
