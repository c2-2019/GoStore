# Dependencies
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Variables
TRIG = 4
ECHO = 18
start = 0
end = 0

# Setup and capture triggers
GPIO.setup(TRIG, GPIO.OUT)  # send out a burst
GPIO.setup(ECHO, GPIO.IN)  # capture it

GPIO.output(TRIG, True)
time.sleep(0.0001)
GPIO.output(TRIG, False)

# Detect start time
while GPIO.input(ECHO) == False:
    start = time.time()

# Detect end time
while GPIO.input(ECHO) == True:
    end = time.time()

sig_time = end - start

# Detect distance in cm
distance = sig_time / 0.000058

# Print distance
print('Distance is: {} cm'.format(distance))

#API call to capture photo using camera should go here


#API call to add product to cart should go here

#Reset GPIO
GPIO.cleanup()
