#! /usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess

class multiplexer():

    def __init__(self):
        self.multiplexPins = [12, 13, 15, 16, 18, 22, 29]
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD) # set hardware pin numbering


        GPIO.setup(self.multiplexPins, GPIO.OUT)


    def sendcommand(self, output, command):
        GPIO.output(output, True)
        pass # placeholder for ir send command
        GPIO.output(output, False)




def main():
    pass

if __name__ == '__main__':
    mult = multiplexer()
    main()
