import RobotApi as ap

def connect():
	ap.ubtRobotInitialize()
	ap.ubtRobotConnect('sdk','1','127.0.0.1')

def stop():
	ap.ubtSetRobotLED('button','blue','breath')
	ap.ubtStopRobotAction()
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')
	ap.ubtRobotDeinitialize()

def left():
	ap.ubtSetRobotMotion('raise','left',3,1)
	ap.ubtSetRobotLED('button','yellow','blink')

def right():
	ap.ubtSetRobotMotion('raise','right',3,1)
	ap.ubtSetRobotLED('button','green','blink')

def main():
	connect()
	while(True):
		f = open('model.txt','r')
		a = f.read(1)
		if (a == 1):
			left()
		elif (a ==  2):
			right()
		elif (a == 3):
			break
		else:
			pass
	f.close()
	stop()

if __name__ == '__main__':
	main()
	