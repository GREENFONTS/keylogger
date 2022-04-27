# Keylogger

This python project is a keylogger application that collects data from a PC and sends the documents it to a specified email. It does performs this task continously. It is a form of a spyware or monitoring system. The data collect includes:
- Keyboard input
- Clipboard data
- Sound Recording 
- Screenshots of the PC
- System software and hardware information

## TECHNOLOGIES AND LIBRARIES USED
- [Python](https://www.python.org/downloads/)
- [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.1/installation.html)
- [psutil](https://pypi.org/project/psutil/)
- [Tkinter](https://tkdocs.com/)
- [Pynput](https://pypi.org/project/pynput/)
- [pyscreenshot](https://pypi.org/project/pyscreenshot/)
- [smtplib](https://pypi.org/project/secure-smtplib/)

### To test the code:
- Fork the repo and clone it.
- Install python if not installed
- Run ```py setup.py install``` to install the necessary dependencies
- Go to config.py file and assign the environmental variables, email and password for sending the files
- From a terminal and inside the project directory - run ```py main.py``` to start the keylogger