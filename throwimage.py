import os
import time
from random import randint
import cv2
filelist=[]
global count
count=0
while True:
	for file in os.listdir("/Users/Nathan/OneDrive/Code/codestellation/images"):
		if file not in filelist and file[0]!=".":
			filelist.append(file)
	num=randint(0,9)
	if len(filelist)>0 and len(filelist)!=count:
		temp="/Users/Nathan/OneDrive/Code/codestellation/images/"+filelist[-1]
		img=cv2.imread(temp,1)
		

		a="/Users/Nathan/OneDrive/Code/codestellation/readyoutput/output"+str(num)+".jpg"
		cv2.imwrite(a,img)
		count=len(filelist)

		time.sleep(5)