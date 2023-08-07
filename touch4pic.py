import os
import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)
touch_pin = 12
GPIO.setup(touch_pin, GPIO.IN)

picture_folder = "pictures"  # Folder name to save the pictures

def create_folder():
    if not os.path.exists(picture_folder):
        os.makedirs(picture_folder)

def capture_image():
    with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)  # Set the resolution to 1920x1080 (Full HD)
        time.sleep(2)  # Allow the camera to warm up
        create_folder()
        image_file = os.path.join(picture_folder, f"captured_image_{int(time.time())}.jpg")
        camera.capture(image_file)
    return image_file

def beep():
    os.system("echo -e '\a'")

try:
    while True:
        if GPIO.input(touch_pin):
            print("Touch detected! Taking a new picture.")
            beep()
            image_file = capture_image()
            print(f"Image saved as '{image_file}'")
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
