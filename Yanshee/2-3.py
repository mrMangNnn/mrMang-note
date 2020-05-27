#-*-coding:utf-8-*-

import RobotApi as ap
import time

def connect():
	ap.ubtRobotInitialize()
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')

def stop():
	ap.ubtStopRobotAction()
	ap.ubtSetRobotLED('button','blue','breath')
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')
	ap.ubtRobotDeinitialize()

def read_value():
	touch = ap.UBTEDU_ROBOTTOUCH_SENSOR_T()
	ap.ubtReadSensorValue('touch',touch,4)
	return(touch.iValue)

def touch():
	ap.ubtSetRobotMotion('raise','left',3,1)
	ap.ubtVoiceTTS(1,'很高兴认识你，人类朋友')

def main():
	count = 0
	while(True):
		time.sleep(0.5)
		count += 1
		if read_value() != 0:
			touch()
		if count == 20:
			break

if __name__ == '__main__':
	connect()
	main()
	stop()
