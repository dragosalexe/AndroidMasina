import RPi.GPIO as GPIO
import time

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(7, False)
	GPIO.output(11, False)
	GPIO.output(16, False)
	GPIO.output(18, False)

def ServoUp():
	init()
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(16, True)
	GPIO.output(18, False)

def StopMotor():	
	init()
	GPIO.cleanup()

def ServoDown():
	init()
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(16, False)
        GPIO.output(18, True)

def SpateVoce():
        init()
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(16, False)
        GPIO.output(18, True)
	time.sleep(1)
	GPIO.cleanup()	

def ServoDreapta():
        init()
        print('Dreapta')
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(16, True)
        GPIO.output(18, False)
def DreaptaVoce():
        init()
        print('Dreapta')
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(16, True)
        GPIO.output(18, False)
	time.sleep(1)
	GPIO.cleanup()

def ServoStanga():
	init()
	print('Stanga')
	GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(16, False)
        GPIO.output(18, True)

def StangaVoce():
        init()
        print('Stanga')
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(16, False)
        GPIO.output(18, True)
        time.sleep(1)
        GPIO.cleanup()



def ServoUpVoce():
        init()
	print('Inainte Voce')
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(16, True)
        GPIO.output(18, False)
	time.sleep(1)
	GPIO.cleanup()

