# import the library
import cv2

# read the image
img=cv2.imread("rainbow_wheel.jpg",0)

# creating a binary threshold 
# separates the image into two regions of binary
_, th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# creating truncate threshold
# creates a trunc after the threshold value is reached 
_, th2=cv2.threshold(img,160,255,cv2.THRESH_TRUNC)

# zeroes the value till the threshold value is reached
_, th3=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

#displaying the original image and the thresholds
cv2.imshow("image",img)
cv2.imshow("binary threshold",th1)
cv2.imshow("Trunc threshold",th2)
cv2.imshow("To zero threshold",th3)

#creating a waitkey
cv2.waitKey(0)
cv2.destroyAllWindows