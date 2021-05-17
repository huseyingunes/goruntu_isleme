import cv2 as cv
import numpy as np

capture = cv.VideoCapture("video/rat.avi")
lower_white = np.array([0, 0, 0])
upper_white = np.array([360, 300, 200])

while(True):
    ret, frame = capture.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #print(nisangah.shape)  # video boyutu 600,800
    kirp = hsv[40:570, 230:770]
   # print(kirp.shape)  #530,540
    mask = cv.inRange(kirp, lower_white, upper_white)
    res = cv.bitwise_and(kirp, kirp, mask=mask)
    #cv.imshow("frame", kirp)
    cv.imshow("mask", mask) #beyaz taban siyah fare!!!!
    #cv.imshow("res", res)
    if cv.waitKey(1) == ord('q'):
        break
# 15 puan