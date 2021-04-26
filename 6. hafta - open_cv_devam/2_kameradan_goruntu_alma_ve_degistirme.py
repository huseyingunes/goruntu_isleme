import cv2 as cv

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret:
        cv.imshow("kamera", gray)
        if cv.waitKey(33) == ord('q'):
            break

