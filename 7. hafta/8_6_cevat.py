import cv2 as cv
import numpy as np

video = cv.VideoCapture("video/rat.avi")
lower = np.array([0, 0, 0])
upper = np.array([255, 250, 250])

while video.isOpened():
    ret, frame = video.read()
    frame2 = frame[35:570, 225:770]
    hsv = cv.cvtColor(frame2, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    res = cv.bitwise_and(frame2, frame2, mask=mask)
    res = cv.bitwise_not(frame2, res, mask=mask)
    cv.imshow("res", res)
    if cv.waitKey(33) == ord('q'):
        break
