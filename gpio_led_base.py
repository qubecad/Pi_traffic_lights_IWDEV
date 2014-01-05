
# IWDEV Pi Blinking LED

import RPi.GPIO as GPIO
import time


# set GPIO Mode

GPIO.setmode(GPIO.BCM)

# set pin mode
GPIO.setup(02,GPIO.OUT)


# set inital pin state

GPIO.output(02,False)



# start a loop to control the lights.

while True:
    print "Red on"
    GPIO.output(02,True)
    time.sleep(1)
    print "Red off"
    GPIO.output(02,False)
    time.sleep(1)

    
