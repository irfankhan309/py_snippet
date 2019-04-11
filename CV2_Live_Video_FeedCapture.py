import cv2

def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:

        ret, frame = cap.read()

        # this two lines is for GRAY Captured video
        # op = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # cv2.imshow('grey video',op)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.distroyWindow(windowName)

    cap.release()

if __name__ =="__main__":
    main()