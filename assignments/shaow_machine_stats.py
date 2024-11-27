"""
Python CLI to get machine stats
Tested platforms: Windows, Ubuntu

__author__ = Anurag Gundappa
__date__ = 13/09/24
"""

import platform
import psutil
import argparse


def _is_valid_disk(device):
    return not ("cdrom" in device.opts or "nfs" in device.opts)

def _get_processes():
    process_list = []
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            if proc.info['name'] != "System Idle Process":
                process_list.append((proc.info['name'], proc.cpu_percent()))
        except Exception:
            pass
    return sorted(process_list, key=lambda x: x[1], reverse=True)

def get_stats():
    computer_name = platform.node()
    total_physical_memory = psutil.virtual_memory().total / (1024 * 1024 * 1024)
    total_physical_processors = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)
    total_hard_disks =  len([x for x in psutil.disk_partitions() if _is_valid_disk(x)])
    top_five_process = _get_processes()[:5]
    return computer_name, total_physical_memory, total_physical_processors, total_cores, total_hard_disks, top_five_process

def show_stats():
    """
    Show machine stats
    """
    computer_name, total_physical_memory, total_physical_processors, total_cores, total_hard_disks, top_five_process = get_stats()
    print(f"Computer Name: {computer_name}\n")
    print(f"Total Physical Memory: {total_physical_memory:.2f} GB\n")
    print(f"Total Number of Physical Processors: {total_physical_processors}\n")
    print(f"Total Number of Cores: {total_cores}\n")
    print(f"Total Number of Hard Disks: {total_hard_disks}\n")
    print(f"Top 5 Processes in terms of CPU: \n")
    for process in top_five_process:
        print(f"\tProcess Name: {process[0]} CPU Usage: {process[1]}")


def log_stats():
    """
    Log machine stats to a file
    """
    log_file = "NiceTestApp.log"

    computer_name, total_physical_memory, total_physical_processors, total_cores, total_hard_disks, top_five_process = get_stats()
    with open(log_file, "w") as f:
        f.write(f"Computer Name: {computer_name}\n")
        f.write(f"Total Physical Memory: {total_physical_memory:.2f} GB\n")
        f.write(f"Total Number of Physical Processors: {total_physical_processors}\n")
        f.write(f"Total Number of Cores: {total_cores}\n")
        f.write(f"Total Number of Hard Disks: {total_hard_disks}\n")
        f.write(f"Top 5 Processes in terms of CPU:\n")
        for process in top_five_process:
            f.write(f"\tProcess Name: {process[0]} CPU Usage: {process[1]}\n")



if __name__ == "__main__":
    # Driver code
    parser = argparse.ArgumentParser(description="A simple CLI to retrieve machine statistics.")
    parser.add_argument('--loginfo', action='store_true', help='Log machine info to a file and display stats')

    args = parser.parse_args()

    if not args.loginfo:
        show_stats()
    else:
        show_stats()
        log_stats()
