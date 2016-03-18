# -*- coding: utf-8 -*-
import os
import requests
import json,time,string
import RPi.GPIO as GPIO

#get(url, params=None, **kwargs)
#requests.get('http://api.yeelink.net/v1.0/device/18483/sensor/32227/datapoints',apiheaders)

apiheaders={'U-ApiKey':'92b42ca8154dde5a3045530e3e5b9815'}

yee_pic_upload_apiurl='http://api.yeelink.net/v1.0/device/18483/sensor/365068/photos'

if __name__ == '__main__':
	while 1:
		#数据上传提取解码查字典，最后得value值即为虚拟开关value的值
		#print '我'  #此行OK
		files={'file': open('ocr_pi.png','rb')}

		r=requests.post(yee_pic_upload_apiurl,files=files,headers=apiheaders)
		print 'r=',r
		print '\n'

		time.sleep(15)

