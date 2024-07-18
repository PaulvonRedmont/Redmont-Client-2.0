from ppadb.client import Client as AdbClient
from PIL import Image
import os, time, pytesseract
from spellchecker import SpellChecker
import cv2
import shutil

wee_little_boxes_file_paths = []

ocr_text = []


message_to_write = ''
latest_screenshot = ''

tesseract_path = r'C:\Users\paule\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

adb_path = r"C:\Users\paule\Downloads\platform-tools-latest-windows\platform-tools\adb.exe"
bluestacks_ip = 'localhost'
bluestacks_port = 5555

time_to_initialize_ADB_client = 0
time_to_screenshot = 0
time_to_copy_screenshot = 0

total_time_for_total_operation = 0
time_to_start_server = 0
time_to_connect_to_server = 0
time_to_kill_server = 0

def append_text_to_file(filename, text):
    with open(filename, 'a') as file:
        timestamp = time.time()
        file.write(text + '\n')
        file.write(f"Message from Alexa written to file at {timestamp}" + '\n')

def start_adb_server():
    global time_to_start_server
    os.system('cls' if os.name == 'nt' else 'clear')
    start_time = time.time()
    os.system(f'{adb_path} start-server')
    time.sleep(2)  # Wait for the server to start
    end_time = time.time()
    total_time = end_time - start_time
    time_to_start_server = total_time
    print(f"It took {time_to_start_server} seconds to start the server")

def connect_to_bluestacks(client):
    global time_to_connect_to_server
    start_time = time.time()
    client.remote_connect(bluestacks_ip, bluestacks_port)
    time.sleep(2)  # Wait for the connection to establish
    end_time = time.time()
    total_time = end_time - start_time
    time_to_connect_to_server = total_time
    print(f"It took {time_to_connect_to_server} seconds to connect to the server")

def stop_adb_server():
    global time_to_kill_server
    start_time = time.time()
    os.system(f'{adb_path} kill-server')
    end_time = time.time()
    total_time = end_time - start_time
    time_to_kill_server = total_time
    print("ADB server stopped.")
    print(f"It took {time_to_kill_server} seconds to stop the server")

def start_connect_to_and_kill_server():
    global time_to_start_server, time_to_connect_to_server, time_to_kill_server, total_time_for_total_operation
    try:
        start_adb_server()
        client = AdbClient(host='127.0.0.1', port=5037)
        connect_to_bluestacks(client)
        devices = client.devices()
        print(f'Connected devices: {devices}')
        print(f"Starting server took {time_to_start_server} seconds.")
        print(f"Connecting to server took {time_to_connect_to_server} seconds.")
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        stop_adb_server()
        total_time_for_total_operation = time_to_start_server + time_to_connect_to_server + time_to_kill_server
        print(f"It took {total_time_for_total_operation} seconds to start, connect to, and kill the server")
        time_to_start_server = 0
        time_to_connect_to_server = 0
        time_to_kill_server = 0

def ONLY_start_and_connect_to_server():
    global time_to_start_server, time_to_connect_to_server, time_to_kill_server, total_time_for_total_operation
    try:
        start_adb_server()
        client = AdbClient(host='127.0.0.1', port=5037)
        connect_to_bluestacks(client)
        devices = client.devices()
        print(f'Connected devices: {devices}')
        print(f"Starting server took {time_to_start_server} seconds.")
        print(f"Connecting to server took {time_to_connect_to_server} seconds.")
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        total_time_for_total_operation = time_to_start_server + time_to_connect_to_server + time_to_kill_server
        print(f"It took {total_time_for_total_operation} seconds to ONLY start and connect to the server")
        time_to_start_server = 0
        time_to_connect_to_server = 0
        time_to_kill_server = 0




def find_and_crop_bubbles(target_image_path, output_folder):
    global wee_little_boxes_file_paths, latest_screenshot
    # Start the timer
    start_time = time.time()
    # Load the target image
    target_image = cv2.imread(target_image_path)
    if target_image is None:
        raise ValueError("Could not load the image. Please check the image path.")
    print(f"Time taken to load the image: {time.time() - start_time} seconds")

    # Convert the image to grayscale
    start_time = time.time()
    gray_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    print(f"Time taken to convert the image to grayscale: {time.time() - start_time} seconds")

    # Apply GaussianBlur to reduce noise and improve edge detection
    start_time = time.time()
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    print(f"Time taken to apply GaussianBlur: {time.time() - start_time} seconds")

    # Apply Canny edge detection
    start_time = time.time()
    edges = cv2.Canny(blurred_image, 50, 150)
    print(f"Time taken to apply Canny edge detection: {time.time() - start_time} seconds")

    # Find contours in the edge-detected image
    start_time = time.time()
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Time taken to find contours: {time.time() - start_time} seconds")

    # Sort the contours based on the y-coordinate of the bounding box (from greatest to smallest y-coordinate)
    start_time = time.time()
    contours = sorted(contours, key=lambda cnt: cv2.boundingRect(cnt)[1], reverse=True)
    print(f"Time taken to sort contours: {time.time() - start_time} seconds")

    # Ensure the output folder exists
    start_time = time.time()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print(f"Time taken to check and create output folder: {time.time() - start_time} seconds")

    count = 0
    messages = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012"]

    # Loop over the contours and save the bounding boxes with labels
    for contour in contours:
        # Get the bounding box for the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Optional: Filter out small contours that are likely not text bubbles
        if w < 50 or h < 50:
            continue

        # Crop the box from the image
        start_time = time.time()
        cropped_box = target_image[y:y+h, x:x+w]
        print(f"Time taken to crop the box from the image: {time.time() - start_time} seconds")

        # Save the cropped box with a labeled filename
        start_time = time.time()
        label = messages[count % len(messages)]  # Select the appropriate label based on count
        timestamp = time.time()
        output_filename = f'cropped_box_{timestamp}_{label}.png'
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, cropped_box)
        print(f"Time taken to save the cropped box: {time.time() - start_time} seconds")
        wee_little_boxes_file_paths.append(output_path)
        count += 1

    print("wee_little_boxes_file_paths:", wee_little_boxes_file_paths)
    


def crop_below_line(image_path, output_folder):
    global latest_screenshot
    all_screenshots = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\All Screenshots"
    cropped_screenshots = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Cropped Screenshots"
    try:
        new_file_path_of_image_to_crop = shutil.copy(image_path, cropped_screenshots)
        print("Copied image to cropping folder")        
        #last_part = os.path.basename(latest_screenshot)
        #image_to_crop_path = os.path.join(cropped_screenshots, f'{last_part}')
    except Exception as e:
        print(f"Error occurred while copying file: {e}")
    # Load the image
    begin_time = time.time()
    image = cv2.imread(new_file_path_of_image_to_crop)
    if image is None:
        raise FileNotFoundError(f"Image file not found: {new_file_path_of_image_to_crop}")
    # Get image dimensions
    height, width, channels = image.shape
    # Define the y-coordinate to crop below
    y_crop = 1636 # assuming you're not using any other type of bluestacks thingy
    # Crop the image
    cropped_image = image[0:y_crop, :]
    # Save the cropped image, overwriting the latest_screenshot
    cv2.imwrite(new_file_path_of_image_to_crop, cropped_image)
    latest_screenshot = new_file_path_of_image_to_crop
    end_time = time.time()
    total_time = end_time - begin_time
    print(f"Cropped image saved to: {new_file_path_of_image_to_crop}")
    print(f"It took {total_time} seconds to crop imag")


def resize_image(file_path, target_size):
    global latest_screenshot
    image = Image.open(file_path)
    resized_image = image.resize(target_size, Image.BICUBIC)
    return resized_image

def OCR_screenshot(file_paths):
    global latest_screenshot, wee_little_boxes_file_paths, ocr_text
    for file_path in file_paths:
        try:
            resized_image = resize_image(file_path, (9000, 6000))  # Resize the image to 9000x6000 pixels
            begin_time = time.time()
            text = pytesseract.image_to_string(resized_image, lang='eng')
            end_time = time.time()
            total_time = end_time - begin_time
            print(f"OCR result for {file_path}: {text}")
            print(f"OCR Completed in {total_time:.5f} seconds")
            text_file_to_write_to = r"C:\Users\paule\Desktop\Redmont-Client-main\Redmont-Client-main\OCR And Logs\message_logs.txt"
            ocr_text.append(text)
            append_text_to_file(text, text_file_to_write_to)
        except Exception as e:
            print(f'An error occurred processing {file_path}: {e}')



def connect_and_screenshot():
    global time_to_initialize_ADB_client, time_to_screenshot, time_to_copy_screenshot, latest_screenshot
    try:
        start_adb_server()
        start_time = time.time()
        client = AdbClient(host='127.0.0.1', port=5037)
        devices = client.devices()
        if not devices:
            raise Exception('No devices/emulators found. Perhaps ye need to (re)launch Bluestacks?')
        device = devices[0]
        end_time = time.time()
        time_to_initialize_ADB_client = end_time - start_time

        start_time = time.time()
        timestamp = time.time()
        remote_screenshot_path = '/sdcard/screenshot.png'
        folder_path = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\All Screenshots"
        local_screenshot_path = os.path.join(folder_path, f'local_screenshot{timestamp}.png')
        latest_screenshot = local_screenshot_path
        print(f"Latest screenshot: {latest_screenshot}")
        device.shell(f'screencap -p {remote_screenshot_path}')
        end_time = time.time()
        time_to_screenshot = end_time - start_time

        start_time = time.time()
        device.pull(remote_screenshot_path, local_screenshot_path)
        device.shell(f'rm {remote_screenshot_path}')
        end_time = time.time()
        time_to_copy_screenshot = end_time - start_time

        print(f"Screenshots saved to {local_screenshot_path}.")
        print(f"It took {time_to_initialize_ADB_client} seconds to initialize ADB client.")
        print(f"It took {time_to_screenshot} seconds to take a screenshot.")
        print(f"It took {time_to_copy_screenshot} seconds to copy and delete the screenshot.")

    except Exception as e:
        print(f'An error occurred: {e}')
        error_message = str(e)
        if "WinError 10061" in error_message:
            print("Trying to resolve error...")
            stop_adb_server()
            ONLY_start_and_connect_to_server()
            connect_and_screenshot()
        else:
            print(f'An error occurred: {e}')

def connect_and_tap(x, y):
    try:
        start_adb_server()
        client = AdbClient(host='127.0.0.1', port=5037)
        client.remote_connect(bluestacks_ip, bluestacks_port)
        devices = client.devices()
        if not devices:
            raise Exception('No devices/emulators found.')
        device = devices[0]
        device.shell(f'input tap {x} {y}')
        print(f"Tapped at {x} {y}")
    except Exception as e:
        print(f'An error occurred: {e}')
        error_message = str(e)
        if "WinError 10061" in error_message:
            print("Trying to resolve error...")
            stop_adb_server()
            ONLY_start_and_connect_to_server()
            connect_and_tap(x, y)
        else:
            print(f'An error occurred: {e}')

def connect_and_type(x, y, message):

    try:
        #start_adb_server()
        client = AdbClient(host='127.0.0.1', port=5037)
        client.remote_connect(bluestacks_ip, bluestacks_port)
        devices = client.devices()
        if not devices:
            raise Exception('No devices/emulators found.')
        device = devices[0]
        device.shell(f'input tap {x} {y}')
        print(f"Tapped at {x} {y}")
        time.sleep(1)
        device.shell(f'input text "{message}"')
        print(f"Successfully entered {message}")
        time.sleep(1)
        device.shell('input keyevent 66')
        print("Successfully pressed ENTER and hopefully sent the message")
    except Exception as e:
        print(f'An error occurred: {e}')
        error_message = str(e)
        if "WinError 10061" in error_message:
            print("Trying to resolve error...")
            stop_adb_server()
            ONLY_start_and_connect_to_server()
            connect_and_type(x, y, message)
        else:
            print(f'An error occurred: {e}')



def main():
    pass
    #stop_adb_server() # This is for testing, to see how the script can handle the errors and restart the server.
    #connect_and_type(500, 1800, "Quick fight")
    cropped_images_folder = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Cropped Screenshots"
    individual_messages_folder = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Individual Messages"
    connect_and_screenshot()
    crop_below_line(latest_screenshot, cropped_images_folder)
    find_and_crop_bubbles(latest_screenshot, individual_messages_folder)
    #OCR_screenshot(wee_little_boxes_file_paths)

main()
