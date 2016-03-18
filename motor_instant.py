#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import sys
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

p=GPIO.PWM(4,500)

p.start(50)

#p.start(float(sys.argv[1]))
time.sleep(0.3)

while True:
	cmd = raw_input("Commands p pause/s start/k kill:")
	direction = cmd[0]
	if direction == "p" :
			p.start(50)
	elif 	direction == 's' :
		speed = int(cmd[1])*10+int(cmd[2])+int(cmd[3])*0.1
		if speed > 90 :
			speed = 90	
		p.start(speed)
	elif	direction == 'k' :
		break
	else : print ("Invalid Input")
p.stop()
GPIO.cleanup()
