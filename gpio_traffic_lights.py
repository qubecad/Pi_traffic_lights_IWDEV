
# IWDEV Pi Traffic lights

import RPi.GPIO as GPIO
import time


# set GPIO Mode

GPIO.setmode(GPIO.BCM)

# set pin mode
GPIO.setup(02,GPIO.OUT)
GPIO.setup(03,GPIO.OUT)
GPIO.setup(04,GPIO.OUT)

# set inital pin state

GPIO.output(02,False)
GPIO.output(03,False)
GPIO.output(04,False)


# start a loop to control the lights.

while True:
    print "Red on"
    GPIO.output(02,True)
    time.sleep(1)
    print "Red off"
    GPIO.output(02,False)
    time.sleep(1)
    
    print "Amber on"
    GPIO.output(03,True)
    time.sleep(1)
    print "Amber off"
    GPIO.output(03,False)
    time.sleep(1)
    
    print "Green on"
    GPIO.output(04,True)
    time.sleep(1)
    print "Green off"
    GPIO.output(04,False)
    time.sleep(1)
    
