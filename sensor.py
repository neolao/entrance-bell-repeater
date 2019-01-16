#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import urllib2

SensorPin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SensorPin, GPIO.IN)

def callback(channel):
        urllib2.urlopen("http://10.0.1.36:8080")

GPIO.add_event_detect(SensorPin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(SensorPin, callback)  # assign function to GPIO PIN, Run function on change

while True:
        time.sleep(1)

