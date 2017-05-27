#! /usr/bin/env python3

import RPi.GPIO as GPIO

driverPin = 11
multiplexPins = [12, 13, 15, 16, 18, 22, 29]

def setup():
    GPIO.setmode(GPIO.BOARD) # set hardware pin numbering

    GPIO.setup(driverPin, GPIO.OUT, False)# set lirc driver pin

    for item in multiplexPins:
        GPIO.setup(item, GPIO.OUT, False)



def main():
    pass

if __name__ == '__main__':
    main()
