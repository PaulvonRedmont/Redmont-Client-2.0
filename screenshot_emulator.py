from ppadb.client import Client as AdbClient
from Connect_to_emulator import ONLY_start_and_connect_to_server
#from Connect_to_emulator import start_connect_to_and_kill_server
import os, time

adb_path = r"path to adb.exe"
bluestacks_ip = 'localhost'
bluestacks_port = 5555

time_to_initialize_ADB_client = 0
time_to_screenshot = 0
time_to_copy_screenshot = 0
time_to_kill_server = 0

def stop_adb_server():
    global time_to_kill_server 
    start_time = time.time()
    os.system(f'{adb_path} kill-server')
    end_time = time.time()
    total_time_to_kill_server = start_time - end_time
    time_to_kill_server = total_time_to_kill_server
    print(f"Server killed in {time_to_kill_server} seconds")


def connect_and_screenshot():
    global time_to_initialize_ADB_client, time_to_screenshot, time_to_copy_screenshot
    try:
        # Initialize ADB client
        start_time = time.time()
        client = AdbClient(host='127.0.0.1', port=5037)
        # Retrieve connected devices/emulators
        devices = client.devices()
        if not devices:
            raise Exception('No devices/emulators found.')
        # Handle multiple devices if needed
        device = devices[0]
        end_time = time.time()
        total_time_to_start_client = start_time - end_time
        time_to_initialize_ADB_client = total_time_to_start_client
        start_time = 0
        end_time = 0
        
        start_time = time.time()
        # Specify paths
        timestamp = time.time()
        remote_screenshot_path = '/sdcard/screenshot.png'
        local_screenshot_path = f'local_screenshot{timestamp}.png'
        # Capture screenshot on the BlueStacks device
        device.shell(f'screencap -p {remote_screenshot_path}')
        print(f'Screenshot saved to {remote_screenshot_path} on the device.')
        end_time = time.time()
        total_time_to_screenshot = start_time - end_time
        time_to_screenshot = total_time_to_screenshot
        start_time = 0
        end_time = 0

        start_time = time.time()
        # Pull the screenshot to the local machine
        device.pull(remote_screenshot_path, local_screenshot_path)
        print(f'Screenshot pulled to {local_screenshot_path} on the local machine.')
        # Delete the screenshot from the emulator
        device.shell(f'rm {remote_screenshot_path}')
        print(f'Screenshot deleted from the device.')
        end_time = time.time()
        total_time_to_copy_screenshot = start_time - end_time
        time_to_copy_screenshot = total_time_to_copy_screenshot
        start_time = 0
        end_time = 0
        print("")
        print(f"It took {time_to_initialize_ADB_client} seconds to initialize ADB client")
        print(f"It took {time_to_screenshot} seconds to take a screenshot of emulator")
        print(f"It took {time_to_copy_screenshot} seconds to copy screenshot to local machine and delete it from emulator")

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Stop ADB server
        stop_adb_server()

connect_and_screenshot()
