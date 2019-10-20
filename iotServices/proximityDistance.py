# Dependencies
import RPi.GPIO as GPIO
import time

# Common variables
itemPicked=False

# Logic starts
try:
      GPIO.setmode(GPIO.BOARD)

      # Variables
      PIN_TRIGGER = 7
      PIN_ECHO = 11

      GPIO.setup(PIN_TRIGGER, GPIO.OUT) # send out a burst
      GPIO.setup(PIN_ECHO, GPIO.IN) # capture it

      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      
      # Allow break for sensor setup
      print("Setting up proximity sensor...")
      time.sleep(2)
      
      # Getting distance from sensor
      print("Getting distance form sensor...")
      GPIO.output(PIN_TRIGGER, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      # Handling/Calculating distance
      print("Distance recieved, rounding it up...")
      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      
      # Displaying distance
      print("Distance is: ",distance,"cm")
      
      # Checking if an item was taken
      if distance > 3:
          itemPicked=True
          print("An item was taken")
      else:
          print("No items were taken")

finally:
      # Clean GPIO when done
      GPIO.cleanup()
