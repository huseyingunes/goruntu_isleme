import cv2 as cv
import numpy as np

video = cv.VideoCapture("video/F7of.mov")
i = 0
while video.isOpened():
    ret, frame = video.read()
    i+=1
    if i < 270:
        continue
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grayFrame = grayFrame[90:900, 400:1350]
    #grayFrame = cv.medianBlur(grayFrame, 5)
    ret, esiklenmis = cv.threshold(grayFrame, 180, 255,
                                   cv.THRESH_BINARY)
    if ret:
        cv.imshow("fare takip", esiklenmis)
        if cv.waitKey(33) == 27:
            quit()