import RobotApi as ap
import cv2 as cv
import numpy as np

def connect():
	ap.ubtRobotInitialize()
	ap.ubtRobotConnect('sdk','1','127.0.0.1')

def stop():
	ap.ubtSetRobotLED('button','blue','breath')
	ap.ubtStopRobotAction()
	ap.ubtRobotDisconnect('sdk','1','127.0.0.1')
	ap.ubtRobotDeinitialize()

def main():
	cap = cv.VideoCapture(0)
	lower = np.array([23,43,46])
	upper = np.array([44,255,255])
	while(True):
		ret,frame = cap.read()
		frame = cv.resize(frame,(320,240))
		hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
		mask = cv.inRange(hsv,lower,upper)
		open_min = np.ones((5,5),np.uint8)
		open_max = np.ones((7,7),np.uint8)
		erodion = cv.erode(mask,open_min)
		dilation = cv.dilate(erodion,open_max)

		contours,cnt = cv.findContours(dilation.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
		if len(contours) > 0:
			MaxArea = 0
			MaxIndex = 0
			index = -1
			for c in contours:
				index += 1
				area = cv.contourArea(c)
				if area > MaxArea:
					MaxArea = area
					MaxIndex = index
			moment = cv.moments(contours[MaxIndex])
			if moment['m00'] > 0:
				cx = int(moment['m10']/moment['m00'])
				cy = int(moment['m01']/moment['m00'])

			r = np.sqrt(MaxArea/3.14)
			cv.circle(frame,(cx,cy),int(r+0.5),(35,65,43),5)
			h1,w1 = dilation.shape
			f = open('model.txt','w')
			if (1.0*cx/w1 < 0.4):
				f.write('1')
			elif (1.0*cx/w1 > 0.6):
				f.write('2')
			else:
				f.write('3')
		cv.imshow('ball',frame)
		if cv.waitKey(10) & 0xff == ord('q'):
			f = open('model.txt','w')
			f.write('4')
			break
	f.close()

if __name__ == '__main__':
	connect()
	main()
	stop()
