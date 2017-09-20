#!/usr/bin/python

from time import sleep # import the time function from the sleep library
import RPi.GPIO as GPIO # import our GPIO library

GPIO.setmode(GPIO.BCM)
PIR_PIN = 27
LED_PIN = 17
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)

GPIO.output(LED_PIN,GPIO.HIGH)
sleep(1) # sleep for 1 second

# Turn LEDs off
GPIO.output(LED_PIN,GPIO.LOW)
sleep(1)

# Turn LEDs on
GPIO.output(LED_PIN,GPIO.HIGH) 
sleep(1)

# Turn LEDs off
GPIO.output(LED_PIN,GPIO.LOW)

try:
	sleep(2)
	while True:
		if GPIO.input(PIR_PIN):
			GPIO.output(LED_PIN,GPIO.HIGH)
			sleep(1)
		else:
			GPIO.output(LED_PIN,GPIO.LOW)

except KeyboardInterrupt:
	GPIO.output(17,GPIO.LOW)
	GPIO.cleanup()
