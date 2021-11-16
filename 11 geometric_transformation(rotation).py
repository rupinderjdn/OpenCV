#import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
# read the image
img=cv2.imread("virat kohli.jpg")

# getting the shape of the original image
rows=img.shape[0]
cols=img.shape[1]

#creating a rotation matrix
M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

#translating the image
rot=cv2.warpAffine(img,M,(cols,rows))

#displaying the original and rotated image
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(rot),plt.title('Rotated')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()