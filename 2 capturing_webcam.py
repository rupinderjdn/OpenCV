# import the opencv library
import cv2
  
  
# define a video capture object
video = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    return_value, frame = video.read()
  
    # Display the resulting frame
    cv2.imshow('Web Room', frame)
      
    # the 'esc' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1)==27:
        break
  
# After the loop release the cap object
video.release()
# Destroy all the windows
cv2.destroyAllWindows()