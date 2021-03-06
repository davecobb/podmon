#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

# set modes for pins
GPIO.setmode(GPIO.BCM)
LED_PIN = 22
GPIO.setup(LED_PIN,GPIO.OUT)

GPIO.output(LED_PIN,GPIO.HIGH)
sleep(1) # 1 second timeout

# Turn LEDs off
GPIO.output(LED_PIN,GPIO.LOW)
sleep(1)

# Turn LEDs on
GPIO.output(LED_PIN,GPIO.HIGH)
sleep(2)

GPIO.output(LED_PIN,GPIO.LOW)
