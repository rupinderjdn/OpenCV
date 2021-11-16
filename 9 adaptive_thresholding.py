#importing the library
import cv2

#importing image
img=cv2.imread("liam-neesan.jpg",0)

# simple threshold
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#adaptive threshold
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# displaying the original image and the thresholds
cv2.imshow("Image",img)
cv2.imshow("Threshold",th1)
cv2.imshow("Mean",th2)
cv2.imshow("Gaussian",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()