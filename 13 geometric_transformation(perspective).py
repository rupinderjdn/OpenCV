#import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_inline

# read the image and store the shape of the image
img = cv2.imread('virat kohli.jpg')
rows=img.shape[0]
cols=img.shape[1]


pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()