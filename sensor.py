#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import urllib2

SensorPin = 15
GPIO.setmode(GPIO.BOARD)

GPIO.setup(SensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

file = open("/boot/buzz-ip.txt", "r")
buzzIp = file.read().strip()
file.close()


lastCallback = 0
consecutiveCallback = 0
def callback(channel):
  global lastCallback
  global consecutiveCallback
  global buzzIp

  currentTime = int(round(time.time() * 1000))
  if currentTime - lastCallback < 500:
    consecutiveCallback += 1
  else:
    consecutiveCallback = 0

  if consecutiveCallback == 1:
    print("buzz")
    urllib2.urlopen("http://" + buzzIp + ":8080")

  lastCallback = currentTime

  print(str(lastCallback) + " : " + str(consecutiveCallback))

GPIO.add_event_detect(SensorPin, GPIO.BOTH, callback, bouncetime=200)

while True:
        time.sleep(1)

