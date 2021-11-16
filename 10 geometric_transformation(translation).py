#import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
# read the image
img=cv2.imread("virat kohli.jpg")

# getting the shape of the original image
rows=img.shape[0]
cols=img.shape[1]

#creating a translation matrix
M=np.float32([[1,0,30],[0,1,20]])

#translating the image
trs=cv2.warpAffine(img,M,(cols,rows))

#displaying the original and translated image
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(trs),plt.title('Translated')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()