#import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_inline

# read the image and store the shape of the image
img = cv2.imread('virat kohli.jpg')
rows=img.shape[0]
cols=img.shape[1]


pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

trs = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(trs),plt.title('Affined')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()