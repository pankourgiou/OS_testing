import platform

def check_os_info():
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Architecture:", platform.architecture()[0])

check_os_info()

import os

def check_file_permissions(file_path):
    permissions = {
        "readable": os.access(file_path, os.R_OK),
        "writable": os.access(file_path, os.W_OK),
        "executable": os.access(file_path, os.X_OK)
    }
    return permissions

file_path = "/path/to/your/file"
print(check_file_permissions(file_path))

import psutil

def check_cpu_memory():
    # CPU
    print("CPU Usage (%):", psutil.cpu_percent(interval=1))
    print("CPU Cores:", psutil.cpu_count(logical=True))
    
    # Memory
    memory_info = psutil.virtual_memory()
    print("Total Memory (GB):", round(memory_info.total / (1024 ** 3), 2))
    print("Used Memory (%):", memory_info.percent)

check_cpu_memory()

import subprocess

def check_firewall_status():
    try:
        result = subprocess.run(["sudo", "ufw", "status"], capture_output=True, text=True)
        print("Firewall Status:\n", result.stdout)
    except Exception as e:
        print("Error checking firewall:", e)

check_firewall_status()

import psutil

def check_disk_usage(path="/"):
    disk_usage = psutil.disk_usage(path)
    print(f"Total Disk Space (GB): {round(disk_usage.total / (1024 ** 3), 2)}")
    print(f"Used Disk Space (%): {disk_usage.percent}")
    print(f"Free Disk Space (GB): {round(disk_usage.free / (1024 ** 3), 2)}")

check_disk_usage()

import psutil

def list_running_processes():
    print("{:<10} {:<25} {:<10}".format("PID", "Process Name", "Memory (%)"))
    for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_percent']):
        print("{:<10} {:<25} {:<10}".format(proc.info['pid'], proc.info['name'], round(proc.info['memory_percent'], 2)))

list_running_processes()

import psutil

def check_network_info():
    net_info = psutil.net_if_addrs()
    for interface, addrs in net_info.items():
        print(f"Interface: {interface}")
        for addr in addrs:
            print(f"  Address Family: {addr.family}")
            print(f"  IP Address: {addr.address}")
            print(f"  Netmask: {addr.netmask}")
            print(f"  Broadcast: {addr.broadcast}")
        print("\n")

check_network_info()

import psutil
import datetime

def check_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    print("System Boot Time:", boot_time)
    print("System Uptime:", uptime)

check_uptime()

import psutil

def check_logged_in_users():
    users = psutil.users()
    print("{:<15} {:<10} {:<15} {:<20}".format("User", "Terminal", "Host", "Started"))
    for user in users:
        print("{:<15} {:<10} {:<15} {:<20}".format(user.name, user.terminal, user.host, datetime.datetime.fromtimestamp(user.started)))

check_logged_in_users()
