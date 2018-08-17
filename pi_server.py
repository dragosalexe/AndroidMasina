import Servomotor
from socket import *
from time import ctime
import RPi.GPIO as GPIO


Servomotor.init()

ctrCmd = ['F','S','P','R','L','A','B','C','D']

HOST = '192.168.43.181'
PORT = 21565
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print 'Waiting for connection'
        tcpCliSock,addr = tcpSerSock.accept()
        print '...connected from :', addr
       	try:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                Servomotor.ServoUp()
                                print 'Fata'
                        if data == ctrCmd[1]:
                                Servomotor.ServoDown()
                                print 'Spate'
			if data == ctrCmd[2]:
				Servomotor.StopMotor()
				print 'Stop'
			if data == ctrCmd[3]:
				Servomotor.ServoDreapta()
				print 'Dreapta'
			if data == ctrCmd[4]:
				Servomotor.ServoStanga()
				print 'Stanga'
			if data == ctrCmd[5]:
				Servomotor.ServoUpVoce()
				print 'Fata voce'
			if data == ctrCmd[6]:
                                Servomotor.SpateVoce()
                                print 'Spate voce'
			if data == ctrCmd[7]:
                                Servomotor.DreaptaVoce()
                                print 'Dreapta voce'
			if data == ctrCmd[8]:
                                Servomotor.StangaVoce()
                                print 'Stanga voce'
		
        except KeyboardInterrupt:
                Servomotor.close()
                GPIO.cleanup()
tcpSerSock.close();
