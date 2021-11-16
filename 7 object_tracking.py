#import the libraries
import cv2
import numpy as np

# Creating Tracking window
cv2.namedWindow("Tracker")

# An empty callback function for our trackbars
def empty(x):
    pass

# Creating trackbars 
# arguments are:- name of the trackbar, name of the window 
# in which it should be displayed, the set value and then ending value,
# a callback function
cv2.createTrackbar("Low Hue","Tracker",0,255,empty)
cv2.createTrackbar("Low Saturation","Tracker",0,255,empty)
cv2.createTrackbar("Low Value","Tracker",0,255,empty)
cv2.createTrackbar("High Hue","Tracker",255,255,empty)
cv2.createTrackbar("High Saturation","Tracker",255,255,empty)
cv2.createTrackbar("High Value","Tracker",255,255,empty)

# an infinite loop to display our image 
while True:
    frame=cv2.imread("rainbow_wheel.jpg")

    # converting to hsv
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # getting the tracker object for our image
    # arguments are the name of the trackbar and the window
    lh=cv2.getTrackbarPos("Low Hue","Tracker")
    ls=cv2.getTrackbarPos("Low Saturation","Tracker")
    lv=cv2.getTrackbarPos("Low Value","Tracker")
    uh=cv2.getTrackbarPos("High Hue","Tracker")
    us=cv2.getTrackbarPos("High Saturation","Tracker")
    uv=cv2.getTrackbarPos("High Value","Tracker")

    # creating the lower bound and upper bound arrays
    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])

    # creating a mask to detect the colour on the tracker
    mask=cv2.inRange(hsv,lb,ub)

    # performing an and operation on the image and the mask 
    # will work like a normal and operation
    result=cv2.bitwise_and(frame,frame,mask=mask)

    # displaying all the three windows
    cv2.imshow("image",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    # if the 'esc' is pressed close all windows
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()


