# codestellation test in Brandies Univ.
Environment
opencv@2
javascript
python
thanks for info of "Real-time Smile Detection in Python OpenCV"
from: http://pushbuttons.io/blog/2015/4/27/smile-detection-in-python-opencv

Topic:
Read "Smile Face" from computer's camera and output in web page as a matrix

Opportunities:
You can use them on the wedding ceremony. If you have camera, then the program
will scan the images and output everybody's smile on the web page.
If you are using FB live function, you can play the live video on the 
whole screen and let the program to scan the screen to catch the smile face.
But this part is not finished.

Method:
#screenshot.py
We use Python and opencv to load the images of cameras,
and detect if there's "smile face".
If yes, save into directory. 

#throwimage.py
At the meantime, we run a process to detect if there's any new smile images.
If yes, replace the image randomly so we can change the output in web.

#react
Shows the combination of images as matrix in the web page. If the output images
have been replaced, the matrix of images will also be updated.
