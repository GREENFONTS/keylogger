import psutil
import GPUtil
import platform

def system_Data():
    # getting disk info
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        ROM_space = partition_usage.total
    # getting network info
    addrs = psutil.net_if_addrs()
    for interface_name, interface_addrs in addrs.items():
        for address in interface_addrs:
            if str(address.family) == "AddressFamily.AF_INET":
                IP_Address = address.address
                Netmask = address.netmask
                BroadcastIP = address.broadcast
            elif str(address.family) == "AddressFamily.AF_PACKET":
                IP_Address = address.address
                Netmask = address.netmask
                BroadcastIP = address.broadcast
    # getting gpu info
    gpus: list = GPUtil.getGPUs()
    for gpu in gpus:
        try:
            gpu_name = gpu.name
            gpu_memory = gpu.memoryTotal
        except:
            continue
    body = f'''
    ==== The System Information ====\n

    Computer Name : {platform.node()}\n
    Machine Type: {platform.machine()}\n
    Processor : {platform.processor()}\n
    Processor Speed : {psutil.cpu_freq().current / 1000}\n
    Operating System: {platform.system()} {platform.release()}; version : {platform.version()}\n
    Total RAM Installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB\n
    Total RAM Installed: {round(ROM_space/1000000000)} GB\n
    Ip address: {IP_Address}\n
    Netmask: {Netmask}\n
    BroadcastIp : {BroadcastIP}\n
    Installed GPU : {gpu_name if gpus != []  else 'No GPU found'}
    GPU memory: {gpu_memory if gpus != [] else 'No GPU found'}
    '''
    file1 = open('system_Information_file.txt', 'a')
    file1.write(body)
    file1.close()