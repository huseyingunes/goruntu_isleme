import cv2 as cv

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("kamera", gray)
        if cv.waitKey(33) == ord('q'):
            break

