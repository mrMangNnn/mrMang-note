#-*-coding:utf-8-*-

import RobotApi as ap

def connect():
	ap.ubtRobotInitialize()
	ap.ubtRobotConnect('sdk','1','127.0.0.1')

def stop():
	ap.ubtStopRobotAction()
	ap.ubtSetRobotLED('button','blue','breath')
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')
	ap.ubtRobotDeinitialize()

def read_value():
	gyro = ap.UBTEDU_ROBOTGYRO_SENSOR_T()
	ap.ubtReadSensorValue('gyro',gyro,96)
	return(gyro.dEulerxValue)

def getup():
	ap.ubtStartRobotAction('getup_in_back',1)
	ap.ubtVoiceTTS(1,'哎呀，不小心摔倒了，没有人看到吧')

def main():
	while(True):
		a = raw_input('please enter to continue or input q to quit:')
		if a == 'q':
			break
		if read_value() > 140 or read_value() < -140:
			getup()

if __name__ == '__main__':
	connect()
	main()
	stop()
