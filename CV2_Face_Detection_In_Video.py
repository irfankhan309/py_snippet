import cv2
import numpy as np

# creating a video capture object and read from input file.


cap = cv2.VideoCapture('cspace.mp4')
# now creating the face detection in the video

face_cascade =cv2.CascadeClassifier('D:\\cv2_repo\\frontalFace10\\haarcascade_frontalface_default.xml')


# Read until video is completed
while(True):
    # capture frame by frame
    ret, frame = cap.read()
    # convert into the gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect the faces in the video

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw the rectangle boxed around the faces..

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)



    # Result frame
    cv2.imshow('Frame',frame)

    # to exit Q key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# now releasing the videocapture object

cap.release()

# now close frames
cv2.destroyAllWindows()