# Dependencies
import picamera
import time

# Variables
currentTime=time.time()
rootPath='/home/pi/Uni/goStore/iotServices/'
imgPath=rootPath+'capturedImages/'+currentTime+'.jpg'

# Setup camera / close running cameras when done
print("Taking a picture...")

with picamera.PiCamera() as camera:
    camera.resolution=(1280,720)
    camera.capture(imgPath)

print('Picture taken and saved in: '+imgPath)
