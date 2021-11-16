#importing the cv2 library
import cv2

#importing numPy library
import numpy as np

# as all the images are saved as arrays in the computer thus an array
# of zeroes represent a black image.
img=np.zeros([256,256,4],np.uint8)

# Drawng a line on the image it takes 5 major arguments
# image source, starting point, ending point, color int BGR format, thickness
img=cv2.line(img,(0,0),(128,128),(0,0,255),5)

# Drawing an arrowed line, takes the same arguments as the normal line
img=cv2.arrowedLine(img,(0,256),(128,128),(82,168,50),5)

# Drawing a rectangle, the argument it takes are similar to the that of a line 
# but the point of difference is that the starting point is the top-left
# corner of the rectangle and the ending point is the bottom-right 
# corner of the rectangle 
img=cv2.rectangle(img,(160,0),(255,80),(157,50,168),-1)

# Drawing a circle, the argument it takes are as follows :- 
# image source, center co-ordinate, radius, Colour in BGR format, Thickness
# NOTE:- that he thickness=-1 will fill up the figure
img=cv2.circle(img,(170,170),30,(5,234,255),-1)

# Putting up a text on the image, the arguments are:- 
# image source, text to be shown, location, font style, font size, 
# colour in BGR format, thickness, line style
img=cv2.putText(img,"IKUSEI ROCKS !!",(5,100),
        cv2.FONT_HERSHEY_DUPLEX,1,(255,47,5),4,cv2.LINE_AA)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()