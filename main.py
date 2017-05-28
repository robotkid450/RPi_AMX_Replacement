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


    def sendCommand(self, output, command):
        GPIO.output(output, True)
        subprocess.run(command, shell=True, check=True)
        GPIO.output(output, False)





def main():
    pass

if __name__ == '__main__':
    mult = multiplexer()
    main()
