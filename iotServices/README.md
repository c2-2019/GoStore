# GoStore iotServices

## Components
This folder includes the 2 python files that does the following:

### proximityDistance.py:
    
    Using Raspberry pi and a proximity sensor, this could would detect the distance between the sensor and an obstactle
    That's important in order to automatically detect if any product is picked off from the shelf
    
    A specific formula would detect how many products are picked off according to the distance measures
    Once calculated, another python file would run (takePhoto.py) that would do a POST api call to add the specific product to the user cart (while sending a picture of the user)
    

### takePhoto.py:
    
    Using Raspberry pi and a camera sensor, this would take a picture of the current user and do a POST api call to a separate service that would automatically detect the user and add this product to his cart
    
    
## Installation Requirements

    python3 (`sudo apt-get install python3`)
    python3-picamera (`sudo apt-get install python3-picamera`)