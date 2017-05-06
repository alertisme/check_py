# coding=utf-8

import os
import os.path
import re
import requests
from check_A import check
import chardet


# dir = "../subject1_sample/file"
black_list = ['打开手机支付宝', '付款', '支付']

def aliplay_check(text, filename):

	# file = open(dir + '/' + filename, 'rb')
	try:
		# text = file.read()

		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]		
		# print message
		
		for black in black_list:
			if black not in text and black.decode('utf-8', 'ignore').encode('gb2312') not in text:
				return tuple([True, mess[0]])

		return tuple([False, mess[0]+",p"])

	except Exception as e: 
		print "[ERROR] "+str(e)
		exit(0)

	# finally:
	# 	file.close()