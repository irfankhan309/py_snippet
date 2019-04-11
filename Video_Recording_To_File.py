#with cv2 used live webcam feed capturing and storing into the file 

import cv2


def main():
    #this one is window name  
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    #cap is like object for capturing 
    cap = cv2.VideoCapture(0)
    
    #required  path specified to store the captured file 
    filename = "C:\\Users\\IRFAN\\Desktop\\My_Snippets\\Python_Cv2\\clip.avi"

    #codec is an object which is for coding and encoding, we do have multiple formats for that, like WMV2,WMV1,MJPG,DIVX,XVID,H264
    #when specifying the encoding we used cv2 method called videowriteer_fourcc which is fourcc is means four character code
    #when specifying the fourcc passed individual arguments.
    
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 30    #its vision of video which is gives pretty smooth video that is framerate
    resolution =(640,480)

    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)

    if cap.isOpened():
        ret, frame = cap.read()

    else:
        ret = False

    while ret:
        ret, frame =cap.read()

        VideoFileOutput.write(frame)

        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) ==27:
            break
    cv2.destroyAllWindows()
    cap.release()
if __name__ =="__main__":
    main()
