from ppadb.client import Client as AdbClient
import os, time

adb_path = r"path to adb.exe"
bluestacks_ip = 'localhost'
bluestacks_port = 5555

total_time_for_total_operation = 0
time_to_start_server = 0
time_to_connect_to_server = 0
time_to_kill_server = 0


def start_adb_server():
    global time_to_start_server
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
    print(f"It took {time_to_kill_server} seconds to start the server")

def start_connect_to_and_kill_server():
    global time_to_start_server, time_to_connect_to_server, time_to_kill_server, total_time_for_total_operation
    try:
        # Start ADB server
        start_adb_server()
        # Initialize ADB client
        client = AdbClient(host='127.0.0.1', port=5037)
        # Connect to BlueStacks
        connect_to_bluestacks(client)
        # List connected devices
        devices = client.devices()
        print(f'Connected devices: {devices}')
        print('')
        print(f"Starting server took {time_to_start_server} seconds.")
        print('')
        print(f"Connecting to server took {time_to_connect_to_server} seconds.")

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Stop ADB server
        stop_adb_server()
        total_time_for_total_operation = time_to_start_server + time_to_connect_to_server + time_to_kill_server
        print(f"It took { total_time_for_total_operation} seconds to start, connect to, and kill the server")
        time_to_start_server = 0
        time_to_connect_to_server = 0
        time_to_kill_server = 0
        time_to_kill_server = 0

def ONLY_start_and_connect_to_server():
    global time_to_start_server, time_to_connect_to_server, time_to_kill_server, total_time_for_total_operation
    try:
        # Start ADB server
        start_adb_server()
        # Initialize ADB client
        client = AdbClient(host='127.0.0.1', port=5037)
        # Connect to BlueStacks
        connect_to_bluestacks(client)
        # List connected devices
        devices = client.devices()
        print(f'Connected devices: {devices}')
        print('')
        print(f"Starting server took {time_to_start_server} seconds.")
        print('')
        print(f"Connecting to server took {time_to_connect_to_server} seconds.")

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Stop ADB server
        total_time_for_total_operation = time_to_start_server + time_to_connect_to_server + time_to_kill_server
        print(f"It took { total_time_for_total_operation} seconds to ONLY start and connect to the server")
        time_to_start_server = 0
        time_to_connect_to_server = 0
        time_to_kill_server = 0
        time_to_kill_server = 0

ONLY_start_and_connect_to_server()

#start_connect_to_and_kill_server()
