
######
### Hough Transform demo
##  Press 'q' to quit the program (has instances where it may just hang, try and use the task manager in those cases)
### Please uncomment line 12 in case the program hangs for you
#### This has not been tested on a variety of images, so change parameter ranges in the sliders on lines 53-58 for large images
######

import cv2
import numpy as np
# Loads an image
filename='Drawings/1-resized.jpg'
srce = cv2.imread(filename, cv2.IMREAD_COLOR)
# srce = cv2.resize(srce,(256, 256));			##### If the program is hanging / running slow then resize the image / uncomment this line (results will be inconsistent due to the resize, but this program is simply to serve a proof of concept for a training data creation tool)
gray = cv2.cvtColor(srce, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)

D = 0;
minC = 0;
P1 = 0;
P2 = 0;
mnr = 0;
mxr = 0;	
sw = 0;

cv2.namedWindow('image')
cv2.namedWindow('image2')


def track_callback(x):	
	ms = srce.copy();
	D = cv2.getTrackbarPos('dp','image');
	minC = cv2.getTrackbarPos('Min Distance between centers','image');
	P1 = cv2.getTrackbarPos('Canny Thresh High','image');
	P2 = cv2.getTrackbarPos('Acc Threshold','image');
	mnr = cv2.getTrackbarPos('Min radius','image');
	mxr = cv2.getTrackbarPos('Max radius','image');	

	print( str(D) + ", " +str(minC) + ", " + str(P1) + ", " + str(P2) + ", " + str(mnr) + ", "+ str(mxr) + ", " + str(sw) )
	
	det_circ = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,D, minC,P1, P2,mnr, mxr) # 16,18, actual  = 17, actual  = 193
	
	if det_circ is not None:
		det_circ = np.uint16(np.around(det_circ))
		for i in det_circ[0, :]:
			cv2.circle(ms, (i[0], i[1]), 1, (0, 0, 200), 2)
			cv2.circle(ms, (i[0], i[1]),i[2], (255, 0, 0), 1)
	rop = cv2.resize(ms,(682, 682));
	cv2.imshow("image2",rop);
	del ms 
	del rop
	
cv2.createTrackbar('dp','image',1,10,track_callback);
cv2.createTrackbar('Min Distance between centers','image',27,100,track_callback);
cv2.createTrackbar('Canny Thresh High','image',1,100,track_callback);
cv2.createTrackbar('Acc Threshold','image',1,255,track_callback);
cv2.createTrackbar('Min radius','image',1,100,track_callback);
cv2.createTrackbar('Max radius','image',1,100,track_callback);


mon = 0;

while(1):
#	print( str(D) + ", " +str(minC) + ", " + str(P1) + ", " + str(P2) + ", " + str(mnr) + ", "+ str(mxr) + ", " + str(sw) )
	D = cv2.getTrackbarPos('dp','image');
	minC = cv2.getTrackbarPos('Min Distance between centers','image');
	P1 = cv2.getTrackbarPos('Canny Thresh High','image');
	P2 = cv2.getTrackbarPos('Acc Threshold','image');
	mnr = cv2.getTrackbarPos('Min radius','image');
	mxr = cv2.getTrackbarPos('Max radius','image');	
	
	if (cv2.waitKey(0) & 0xFF) == ord('q'):
		break;

cv2.destroyAllWindows();
