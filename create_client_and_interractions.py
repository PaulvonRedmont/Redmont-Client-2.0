from ppadb.client import Client as AdbClient
from PIL import Image
import os, time, pytesseract
from spellchecker import SpellChecker
 
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

def resize_image(file_path, target_size):
    global latest_screenshot
    image = Image.open(file_path)
    resized_image = image.resize(target_size, Image.BICUBIC)
    return resized_image

def OCR_screenshot(file_path):
    global latest_screenshot
    resized_image = resize_image(file_path, (9000, 6000))  # Resize the image to 9000x6000 pixels
    begin_time = time.time()
    text = pytesseract.image_to_string(resized_image, lang='eng')
    end_time = time.time()
    total_time = end_time - begin_time
    print(f"OCR result: {text}")
    print("OCR Completed in {:.5f} seconds".format(total_time))

def connect_and_screenshot():
    global time_to_initialize_ADB_client, time_to_screenshot, time_to_copy_screenshot, latest_screenshot
    try:
        start_adb_server()
        start_time = time.time()
        client = AdbClient(host='127.0.0.1', port=5037)
        devices = client.devices()
        if not devices:
            raise Exception('No devices/emulators found.')
        device = devices[0]
        end_time = time.time()
        time_to_initialize_ADB_client = end_time - start_time

        start_time = time.time()
        timestamp = time.time()
        remote_screenshot_path = '/sdcard/screenshot.png'
        folder_path = r"C:\Users\paule\Desktop\Redmont-Client-main\screenshots\Screenshots for OCR"
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
        start_adb_server()
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
    #stop_adb_server() # This is for testing, to see how the script can handle the errors and restart the server.
    #connect_and_type(500, 120, "Quack")
    connect_and_screenshot()
    OCR_screenshot(latest_screenshot)

main()
