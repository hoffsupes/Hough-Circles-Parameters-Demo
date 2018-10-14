# Hough-Circles-Parameters-Demo
Small GUI demo to see how changing various parameters of the hough circle transform (written in python and OpenCV)

To run: 

    python hough_track.py
  
Place the input image file path in the filename variable on line 12.

Needs a good system to run! cv.HoughCircles() is quite intensive. Proof of basis thing only, no guarantees in terms of accuracy or reliability, use at your own risk.

Press q to quit.

Various sliders denote the 6 parameters using the HOUGH_GRADIENT method, taken from the OpenCV docs:

dp – Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.

minDist – Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.

param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller (sic, I guess they meant that the lesser one is half the larger one)).

Canny edge detection

This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to “sure-edge” pixels, they are considered to be part of edges. Otherwise, they are also discarded. See the image below

param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.

minRadius – Minimum circle radius.

maxRadius – Maximum circle radius.
