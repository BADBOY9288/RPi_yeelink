#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
pins_BCM = [17,18,27,22,23,24,25,4]  
def setup():
	#BCM
	GPIO.setmode(GPIO.BCM)
	#设置所有GPIO输出状态，value=0
	for pin in pins_BCM:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)
def loop():
	while True:
		for x in xrange(1,5000):
			GPIO.output(4,GPIO.LOW)
		for x in xrange(1,5000):
			GPIO.output(4,GPIO.HIGH)
def destroy():
	for pin in pins_BCM:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
		


