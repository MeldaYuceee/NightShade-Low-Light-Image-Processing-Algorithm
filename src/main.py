import cv2
from image_loader import load_image
from enhancement import enhance_contrast
from noise_reduction import reduce_noise
from utils import convert_to_grayscale

IMAGE_PATH = "../sample_images/low_light_1.png"
OUTPUT_PATH = "../output/enhanced_output.jpg"

def run_nightshade():
    image = load_image(IMAGE_PATH)
    gray = convert_to_grayscale(image)

    denoised = reduce_noise(gray)
    enhanced = enhance_contrast(denoised)

    cv2.imwrite(OUTPUT_PATH, enhanced)
    print("Enhanced image saved.")

if __name__ == "__main__":
    run_nightshade()
