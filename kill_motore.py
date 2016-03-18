#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

p=GPIO.PWM(4,500)


p.start(50)
time.sleep(1)
p.stop()
GPIO.cleanup()