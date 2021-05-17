import numpy as np
import cv2 as cv

video=cv.VideoCapture("video/rat.avi")

lower_white = np.array([0, 0, 0])
upper_white = np.array([255, 255, 100])

while True:
    ret,frame=video.read()
    frame2 = frame[:, 200 : 790]
    hsv = cv.cvtColor(frame2, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_white, upper_white)
    cv.imshow('aaaaaaa',mask)

    if cv.waitKey(1)==ord('q'):
        break

#20 puan