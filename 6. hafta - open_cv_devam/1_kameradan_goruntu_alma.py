import cv2 as cv

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    #frame = frame[:, ::-1]
    if ret:
        cv.imshow("kamera", frame)
        if cv.waitKey(2) == ord('q'):
            break
