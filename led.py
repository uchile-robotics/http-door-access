import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
GPIO.setup(led,GPIO.OUT)

contador=0

while True:
	GPIO.output(led,1)
	print "led encendido :)"
	time.sleep(1)
	GPIO.output(led,0)
	print "led apagado :("
	time.sleep(1)	
	contador+=1

	if contador==6:
		break

GPIO.cleanup()





