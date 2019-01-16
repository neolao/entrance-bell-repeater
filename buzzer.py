#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import RPi.GPIO as GPIO
import time

BuzzerPin = 15

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("Buzz ...")
        self.buzz();

    def do_HEAD(self):
        self._set_headers()

    def buzz(self):
        for x in range(10):
           self.beep(0.025)

    def on(self):
        GPIO.output(BuzzerPin, GPIO.LOW)

    def off(self):
        GPIO.output(BuzzerPin, GPIO.HIGH)

    def beep(self, x):
        self.on()
        time.sleep(x)
        self.off()
        time.sleep(x)

def runServer():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    print 'Starting httpd...'
    httpd.serve_forever()

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(BuzzerPin, GPIO.OUT)
        GPIO.output(BuzzerPin, GPIO.HIGH)

def destroy():
        GPIO.output(BuzzerPin, GPIO.HIGH)
        GPIO.cleanup()

if __name__ == '__main__':
        setup()

        try:
                runServer()
        except KeyboardInterrupt:
                destroy()
