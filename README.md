# codestellation test in Brandies Univ.
Environment
opencv@2
javascript
python
react
thanks for info of "Real-time Smile Detection in Python OpenCV"
from: http://pushbuttons.io/blog/2015/4/27/smile-detection-in-python-opencv
Really big help

Topic:
Read "Smile Face" from webcam or video, and output in web page as a matrix of pictures.

Opportunities:
You can use them on the wedding ceremony. If you have camera, then the program
will scan the images and output everybody's smile on the web page.
If you are using FB live function, you can play the live video on the 
whole screen and let the program to scan the screen to catch the smile faces.


Files:
#screenshot.py
We use Python and opencv to load the images of cameras, and detect if there's "smile face".
If yes, save into directory. 
screencatch() is used to take the screenshot, screencatch3() is used to take image from
webcam. If you want to scan a video file, simply do:
cap=cap=cv2.VideoCapture(0)
change "0" into "myvideo.mp4"

#throwimage.py
At the meantime, we run a process to detect if there's any new smile images in directory.
If yes, replace the image in the output directory randomly so we can change the output in web.

#react
Shows the combination of images as matrix in the web page. If the output images
have been replaced, the matrix of images will also be updated. The output images is stored in 
output directory.
