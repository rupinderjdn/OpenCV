#import the opencv library
import cv2

#creating an object of video capture class
video=cv2.VideoCapture(0)

#fourcc defines the data format in which we are going to save our 
# file, for windows the code is "DIVX"
fourcc=cv2.VideoWriter_fourcc(*'XVID')

# create an object of class video writer for saving the video
output=cv2.VideoWriter("My_cam_grayscale.avi",fourcc,20.0,(640,480))

#running an infinite loop
while(True):
    return_value,frame=video.read()

    # changing our coloured video into a grayscale video frame by frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # saving the grayscale video in the directory
    output.write(gray)

    # displaying both the videos
    cv2.imshow("Original",frame)
    cv2.imshow("Grayscale",gray)

    # waiting for the user to press "esc" key
    if cv2.waitKey(1)==27:
        break

# release both the objects after their use is over
video.release()
output.release()
cv2.destroyAllWindows()