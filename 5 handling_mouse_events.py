#importing library
import cv2

# loading the image
img=cv2.imread("christian-bale-red-carpet.jpg")

#displaying the image
cv2.imshow("Batman",img)

#This he function which will catch our mouse events, 
# it takes following arguments :- 
# event that has occurred, x and y co-ordinates, flags, parameters.
def mouse_event(event,x,y,flags,params):
    # checking which mouse event has occured recently
    if event==cv2.EVENT_LBUTTONDOWN:
        lb="left button"
        font=cv2.FONT_HERSHEY_PLAIN
        # displaying the text
        cv2.putText(img,lb,(x,y),font,5,(0,0,255),4,cv2.LINE_AA)
        # displaying the image with the text
        cv2.imshow("Batman",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        rb="right button"
        font=cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img,rb,(x,y),font,5,(0,255,0),4,cv2.LINE_AA)
        cv2.imshow("Batman",img)

#Whenever someone clicks on the image this function is called 
# and it further connects to the function that we have created.
cv2.setMouseCallback('Batman', mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()