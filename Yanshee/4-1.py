#-*-coding:utf-8-*-

import RobotApi as ap
import RPi.GPIO as GPIO
import time
import cv2 as cv

def connect():
	ap.ubtRobotInitialize()
	ap.ubtRobotConnect('sdk','1','127.0.0.1')

def stop():
	ap.ubtSetRobotLED('button','blue','breath')
	ap.ubtStopRobotAction()
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')
	ap.ubtRobotDeinitialize()

def fan_tts():
	ap.ubtVoiceTTS(1,'欢迎回家，已为您打开风扇，祝您生活愉快')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output = (13,1)
	time.sleep(5)
	GPIO.output = (13,0)

def main():
	finish = False
	face_cascade = cv.CascadeClassifier('niubi,xml')
	cap = cv.VideoCapture(0)
	while(True):
		ret,image = cap.read()
		image = cv.resize(image,(320,240))
		image_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
		face = face_cascade.detectMultiScale(image_gray,scaleFactor = 2.0)
		for x in face:
			fan_tts()
			finish = True
			break
		cv.imshow('niubi',image)
		if finish:
			break
		if cv.waitKey(10) & 0xff == ord('q'):
			break

if __name__ == '__main__':
	connect()
	main()
	stop()
