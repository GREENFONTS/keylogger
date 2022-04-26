import sys
from tkinter import Tk

# copying of clipboard textn
def clipboard_func():
    try:
        data = Tk().clipboard_get()
    except Exception:
        data = "no data in clipboard"
    file1 = open('clipboard_file.txt', "a")
    file1.write(data)
    file1.close()

sys.modules[__name__] = clipboard_func