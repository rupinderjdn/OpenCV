#import the open cv library
import cv2

#reading the image from the source as it is present in the same folder
img=cv2.imread("bradley-cooper.jpg",0)

#displaying the image in a separate window shell with it's name given as an argument
cv2.imshow("sample Image",img)

#waitkey is here so that the window does not dissapear after milliseconds and
# wait till we personally close the window.
cv2.waitKey(0)

# after the windows are destryed then the code will run further
cv2.destroyAllWindows()

# Saving the grayscale version of the image we used, providing the name with which
#  we want to save the file.
cv2.imwrite("bradley-cooper-grayscale.jpg",img)