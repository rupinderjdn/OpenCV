import cv2
img=cv2.imread("christian-bale-red-carpet.jpg")

# Displaying the normal image

# getting the shape and size of the original 
# image, so that we can display it on the image
shape=str(img.shape)
size=str(img.size)

# Creating a string of the text with size and shape
text = "Shape : "+shape+" Size : "+size 

# displaying the text which has size and shape
normal_img=cv2.putText(img,text,(0,100),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3,cv2.LINE_AA)
cv2.imshow("Normal Image",normal_img)
cv2.waitKey(0)
cv2.destroyAllWindows

# Adjusting the size of the image

# altering the height and width of the image by 50% 
height = int(img.shape[1]*.5)
width=int(img.shape[0]*.5)

# creating a tuple 'dimensions' which contains the latered height and width
dimensions=(height,width)

# the resize function majorly takes two argument i.e. 
# the image source and the new dimensions
img=cv2.resize(img,dimensions)

# extracting the new size and shape to be displayed on the image
shape=str(img.shape)
size=str(img.size)


text = "Shape : "+shape+" Size : "+size 
adj_img=cv2.putText(img,text,(0,100),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1,cv2.LINE_AA)


cv2.imshow("Adjusted Image",adj_img)
cv2.waitKey(0)
cv2.destroyAllWindows