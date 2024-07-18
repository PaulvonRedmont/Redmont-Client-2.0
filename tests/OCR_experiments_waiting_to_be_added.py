from PIL import Image
import time, pytesseract


latest_screenshot = ''

tesseract_path = r'C:\Users\paule\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def resize_image(file_path, target_size):
    global latest_screenshot
    image = Image.open(file_path)
    resized_image = image.resize(target_size, Image.BICUBIC)
    return resized_image

def OCR_screenshot(file_path):
    global latest_screenshot
    print("Resizing image... please wait.")
    resized_image = resize_image(file_path, (multiplied_size))  # Resize the image to 9000x6000 pixels
    begin_time = time.time()
    text = pytesseract.image_to_string(resized_image, lang='eng')
    end_time = time.time()
    total_time = end_time - begin_time
    print(f"OCR result: {text}")
    print("OCR Completed in {:.5f} seconds".format(total_time))

def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except IOError:
        print(f"Unable to open image '{image_path}'.")
        return None

def multiply_image_size(image_size, factor):
    width, height = image_size
    new_width = width * factor
    new_height = height * factor
    return new_width, new_height

image_path = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Screenshots for OCR\local_screenshot1720183205.3774416.png"  # Replace with the actual path to your image
image_size = get_image_size(image_path)
if image_size:
    print(f"The image size is {image_size[0]} pixels wide and {image_size[1]} pixels high.")
    print(image_size)
    multiplied_size = multiply_image_size(image_size, 10)
    print(f"The multiplied image size is {multiplied_size[0]} pixels wide and {multiplied_size[1]} pixels high.")
    print(multiplied_size)

def main():
    OCR_screenshot(r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Screenshots for OCR\local_screenshot1720183205.3774416.png")


get_image_size(image_path)

main()
