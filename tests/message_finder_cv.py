import cv2
import numpy as np
import os

def find_and_crop_bubbles(target_image_path, output_folder):
    # Load the target image
    target_image = cv2.imread(target_image_path)
    if target_image is None:
        raise ValueError("Could not load the image. Please check the image path.")
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    count = 0
    # Loop over the contours and save the bounding boxes
    for contour in contours:
        # Get the bounding box for the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Optional: Filter out small contours that are likely not text bubbles
        if w < 50 or h < 50:
            continue
        # Crop the box from the image
        cropped_box = target_image[y:y+h, x:x+w]
        # Save the cropped box
        output_path = os.path.join(output_folder, f'cropped_box_{count}.png')
        cv2.imwrite(output_path, cropped_box)
        count += 1
# Usage
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
target_image_path = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Screenshots for OCR\local_screenshot1720183159.9454582.png"  # Replace with the path to your target image file

find_and_crop_bubbles(target_image_path, downloads_folder)
