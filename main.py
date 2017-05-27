#! /usr/bin/env python3

import RPi.GPIO as GPIO

driverPin = 11
multiplexPins = [12, 13, 15, 16, 18, 22, 29]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(17, GPIO.OUT, False)
    GPIO.setup(12, GPIO.OUT, False)

def main():
    pass

if __name__ == '__main__':
    main()
