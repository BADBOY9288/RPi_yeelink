# -*- coding: utf-8 -*-
import os
import requests
import json,time,string
import RPi.GPIO as GPIO

#get(url, params=None, **kwargs)
#requests.get('http://api.yeelink.net/v1.0/device/18483/sensor/32227/datapoints',apiheaders)

apiheaders={'U-ApiKey':'92b42ca8154dde5a3045530e3e5b9815'}

yee_switch_apiurl='http://api.yeelink.net/v1.0/device/18483/sensor/32227/datapoints'

if __name__ == '__main__':
	while 1:
		#数据上传提取解码查字典，最后得value值即为虚拟开关value的值
		#print '我'  #此行OK
		r=requests.get(url=yee_switch_apiurl,headers=apiheaders)
		print 'r=',r
		encoded=r.content
		print 'encoded=',encoded



		decoded=json.loads(encoded)



		value=decoded['value']
		timestamp=decoded['timestamp']
		print 'timestamp=',timestamp
		print 'value=',value
		print '\n'

		time.sleep(1)


		#将value值赋给GPIO口

		pin=4
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,value)

		time.sleep(1)