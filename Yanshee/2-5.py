#-*-coding:utf-8-*-

import RobotApi as ap
import Tkinter

def connect():
	ap.ubtRobotInitialize()
	ap.ubtRobotConnect('sdk','1','127.0.0.1')

def stop():
	ap.ubtStopRobotAction()
	ap.ubtSetRobotLED('button','blue','breath')
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')
	ap.ubtRobotDeinitialize()

def bow():
	ap.ubtSetRobotMotion('bow','front',2,1)

def takephoto():
	ap.ubtTakeAPhoto('liangzai',8)

def main():
	RobotPanel = Tkinter.Tk()
	RobotPanel.title('RobotPanel')
	RobotPanel.geometry('300x300')

	bow1 = Tkinter.Button(RobotPanel,text = 'bow',command = lambda:bow())
	takephoto1 = Tkinter.Button(RobotPanel,text = 'take photo',command = lambda:takephoto())
	bow1.grid(row = 0,column = 1)
	takephoto1.grid(row = 1,column = 1)
	
	Tkinter.mainloop()

if __name__ == '__main__':
	connect()
	main()
	stop()
