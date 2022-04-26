import sys
import pyscreenshot as ImageGrab

# taking screenshot
def screenshot_func(count):
    image = ImageGrab.grab()
    image.save(f"./screenshot.jpg", "JPEG")

sys.modules[__name__] = screenshot_func