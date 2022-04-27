import pyscreenshot as ImageGrab

# taking screenshot
def screenshot_func():
    image = ImageGrab.grab()
    image.save(f"./screenshot.jpg", "JPEG")

