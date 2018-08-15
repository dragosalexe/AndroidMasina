import RPi.GPIO as GPIO
import time

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)

        def ServoUp():
        setup()
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(18, False)
        GPIO.cleanup()

def ServoDown():
        setup()
        GPIO.output(13, True)
        GPIO.output(15, False)
        GPIO.output(16, False)
        GPIO.output(18, True)
        GPIO.cleanup()



