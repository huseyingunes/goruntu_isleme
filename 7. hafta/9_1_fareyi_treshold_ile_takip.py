import cv2 as cv

video = cv.VideoCapture("video/rat.avi")

while (video.isOpened()):
    ret, frame = video.read()
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grayFrame = grayFrame[20:570, 230:770]
    ret, esiklenmis = cv.threshold(grayFrame, 180, 255,
                                   cv.THRESH_BINARY)
    if ret:
        cv.imshow("fare takip", esiklenmis)
        if cv.waitKey(33) == 27:
            quit()
