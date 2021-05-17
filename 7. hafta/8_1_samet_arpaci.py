import cv2 as cv
import numpy as np

video = cv.VideoCapture("video/rat.avi")

lower_white = np.array([0,0,0])
upper_white=np.array((255,10,255))

while(video.isOpened()):
    ret, frame = video.read()
    siyah=frame[20:570,220:765]
    hsv=cv.cvtColor(siyah,cv.COLOR_BGR2HSV)
    mask=cv.inRange(hsv,lower_white,upper_white)
    res=cv.bitwise_and(siyah,siyah,mask=mask)
    ret, esiklenmis = cv.threshold(res, 30, 255, cv.THRESH_BINARY_INV)
    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",esiklenmis)
    if cv.waitKey(1) == ord('q'):
        break

# 20 puan