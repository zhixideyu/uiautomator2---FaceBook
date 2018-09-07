#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time


class Swipeclass(object):


	def __init__ (self, driver):

		self.driver = driver




	# 向上滑动
	def swipeUp(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.5     
		y1 = height * 0.85   
		y2 = height * 0.25

		d.swipe(x1,y1,x1,y2,t)	




	#  '''向下滑动屏幕'''  
	def swipeDown(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.5
		y1 = height * 0.25
		y2 = height * 0.85
		
		d.swipe(x1, y1, x1, y2, t)
