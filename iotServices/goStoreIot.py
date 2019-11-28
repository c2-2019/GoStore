# Dependencies
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import requests

# Common variables
itemPicked = False

# Logic starts
try:
    GPIO.setmode(GPIO.BOARD)

    # Variables
    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)  # send out a burst
    GPIO.setup(PIN_ECHO, GPIO.IN)  # capture it

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    # Allow break for sensor setup
    print("Setting up proximity sensor...")
    time.sleep(2)

    # Getting distance from sensor
    print("Getting distance form sensor...")
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    # Handling/Calculating distance
    print("Distance recieved, rounding it up...")
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)

    # Displaying distance
    print("Distance is: ", distance, "cm")
    print(" ")

    # Login to get Auth Token
    print("Logging you in")

    token = ''

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "username": "marounm@gmail.com",
        "password": "123456"
    }

    r = requests.post(
        "http://ec2-99-80-232-142.eu-west-1.compute.amazonaws.com:9080/api/login",
        json=payload,
        headers=headers
    )

    if(r):
        token = r.json()['token']
        print("You are successfully logged in")

    else:
        print("Couldn't log you in, please try again")

    # Checking if an item was taken
    if distance > 10:
        itemPicked = True
        print("An item was taken")

        # Send API call to add to cart
        print("Adding Pepsi to cart")

        headers = {
            "Authorization": "Bearer "+token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "quantity": 1,
            "productId": "B0001"
        }

        r = requests.post(
            "http://ec2-99-80-232-142.eu-west-1.compute.amazonaws.com:9080/api/cart/add",
            json=payload,
            headers=headers
        )

        print("Pepsi was added to cart")

    else:
        print("No items were taken")

        # Send API call to remove from cart
        print("Removing Pepsi from cart")

        headers = {
            "Authorization": "Bearer "+token,
        }

        r = requests.delete(
            "http://ec2-99-80-232-142.eu-west-1.compute.amazonaws.com:9080/api/cart/B0001",
            headers=headers
        )

        print("Pepsi was removed from cart")

finally:
    # Clean GPIO when done
    GPIO.cleanup()

# Take picture if item was taken
if itemPicked:
    # Setup camera sensor
    print(" ")
    print("Setting up camera sensor...")
    camera = PiCamera()
    camera.start_preview()

    # Allow break to sense the light levels
    print("Opening camera...")
    time.sleep(3)

    # Take still photo
    print("Taking photo...")
    camera.capture(
        "/home/pi/mmData/Uni/iotServices/capturedImages/userImage.jpg")

    print("Photo captured! Stopping camera...")
    camera.stop_preview()

    print(" ")
    print("All Done!")
