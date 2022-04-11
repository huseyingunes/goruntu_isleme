import cv2 as cv

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        #frame = cv.flip(frame, 1)
        cv.imshow("kamera", frame)
        if cv.waitKey(50) == ord('q'):
            break

