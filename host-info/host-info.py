import platform
import socket
from datetime import datetime

def get_system_info():
    # Gather data
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()

    # Print results
    print("--- System Report ---")
    print(f"Date/Time: {current_time}")
    print(f"Hostname:  {hostname}")
    print(f"OS Name:   {os_name}")
    print(f"Release:   {os_release}")
    print(f"Version:   {os_version}")
    print("---------------------")

if __name__ == "__main__":
    get_system_info()
