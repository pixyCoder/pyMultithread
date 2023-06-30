from time import *
from threading import Thread

def controlBox():
	while True:
		print('Box is open')
		sleep(5)
		print('Box is closed')
		sleep(5)

def controlLED():
	while True:
		print('LED is ON')
		sleep(1)
		print('LED is OFF')
		sleep(1)

if '__name == main':
	boxThread = Thread(target=controlBox)
	ledThread = Thread(target=controlLED)
	boxThread.daemon=True
	ledThread.dameon=True
	boxThread.start()
	ledThread.start()
	while True:
		pass
