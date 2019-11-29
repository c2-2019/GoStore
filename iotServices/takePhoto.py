# Dependencies
from picamera import PiCamera
import time

# Setup camera sensor
print("Setting up camera sensor...")
camera = PiCamera()
camera.start_preview()

# Allow break to sense the light levels
print("Opening camera...")
time.sleep(3)

# Take still photo
print("Taking photo...")
camera.capture("/home/pi/mmData/Uni/iotServices/capturedImages/userImage.jpg")

print("Photo captured! Stopping camera...")
camera.stop_preview()

print("All Done!")