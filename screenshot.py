import threading
import cv2
import sys
import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
import time
from threading import Timer

from multiprocessing import Process
global i
i=0
global stack
stack=[]
#this is used to catch video screen
def screencatch():

	global i
	

	while True:	
		#cap = cv2.VideoCapture(0)
		img=ImageGrab.grab()
		img.save('temp.jpg')
		cap=cv2.imread('/Users/Nathan/OneDrive/Code/codestellation/temp.jpg')
		facePath = "/usr/local/Cellar/opencv@2/2.4.13.4/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
		smilePath = "/usr/local/Cellar/opencv@2/2.4.13.4/share/OpenCV/haarcascades/haarcascade_smile.xml"
		faceCascade = cv2.CascadeClassifier(facePath)
		smileCascade = cv2.CascadeClassifier(smilePath)
		#cap.set(3,640)
		#cap.set(4,480)	

		sF = 1.05	
		a="./images/testpic"+str(i)+".jpg"
		frame=cap
		#ret, frame = cap.read() # Capture frame-by-frame
		img = frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor= sF,
			minNeighbors=8,
			minSize=(55, 55),
			flags=cv2.CASCADE_SCALE_IMAGE
			)
			# ---- Draw a rectangle around the faces
		if len(faces)>0:
			print("faces: ",len(faces))
			
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]	
			smile = smileCascade.detectMultiScale(
				roi_gray,
				scaleFactor= 1.5,
				minNeighbors=22,
				minSize=(25, 25),
				flags=cv2.CASCADE_SCALE_IMAGE
				)	
			# Set region of interest for smiles
			if len(smile)>0:
				print("smiles: ",len(smile))
			for (x, y, w, h) in smile:
				i+=1
				#cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
				cv2.imwrite(a,roi_color)
				stack.append(roi_color)
				#print "!!!!!!!!!!!!!!!!!"
				break
		time.sleep(1)


		#cv2.cv.Flip(frame, None, 1)
		#cv2.imshow('Smile Detector', frame)

	cap.release()
	'''
	a="testpic"+str(i)+".jpg"	
	img.save(a)
	i+=1
	time.sleep(0)
	'''
screencatch()




def screencatch3():
	#face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv@2/2.4.13.4/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
	global i
	global stack
	global cap
	cap=cv2.VideoCapture(0)

	facePath = "/usr/local/Cellar/opencv@2/2.4.13.4/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"

	smilePath = "/usr/local/Cellar/opencv@2/2.4.13.4/share/OpenCV/haarcascades/haarcascade_smile.xml"

	faceCascade = cv2.CascadeClassifier(facePath)
	
	smileCascade = cv2.CascadeClassifier(smilePath)	

	cap.set(3,640)
	cap.set(4,480)	

	sF = 1.05	

	while True:	
		#cap = cv2.VideoCapture(0)
		a="./images/testpic"+str(i)+".jpg"

		ret, frame = cap.read() # Capture frame-by-frame
		img = frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor= sF,
			minNeighbors=8,
			minSize=(55, 55),
			flags=cv2.CASCADE_SCALE_IMAGE
			)
			# ---- Draw a rectangle around the faces
		if len(faces)>0:
			print("faces: ",len(faces))
			
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]	
			smile = smileCascade.detectMultiScale(
				roi_gray,
				scaleFactor= 1.5,
				minNeighbors=22,
				minSize=(25, 25),
				flags=cv2.CASCADE_SCALE_IMAGE
				)	
			# Set region of interest for smiles
			if len(smile)>0:
				print("smiles: ",len(smile))
			for (x, y, w, h) in smile:
				i+=1
				#cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
				cv2.imwrite(a,roi_color)
				stack.append(roi_color)
				#print "!!!!!!!!!!!!!!!!!"
				break
		time.sleep(1)


		#cv2.cv.Flip(frame, None, 1)
		#cv2.imshow('Smile Detector', frame)

	cap.release()
	#cv2.destroyAllWindows()


screencatch3()
