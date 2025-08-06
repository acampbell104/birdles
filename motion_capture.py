import os
import time
from picamera import PiCamera
import RPi.GPIO as GPIO

MOTION_PIN = 4
CAPTURE_DIR = "captures"
os.makedirs(CAPTURE_DIR, exist_ok=True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_PIN, GPIO.IN)

camera = PiCamera()
camera.resolution = (1024, 768)

print("📸 Motion detection active...")

try:
    while True:
        if GPIO.input(MOTION_PIN):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            path = os.path.join(CAPTURE_DIR, f"{timestamp}.jpg")
            camera.capture(path)
            print(f"[{timestamp}] Motion detected. Image saved.")
            time.sleep(5)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("❌ Stopped by user.")
finally:
    GPIO.cleanup()
