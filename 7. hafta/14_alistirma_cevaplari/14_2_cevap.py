"""
2 - Kameradan gelen görüntüdeki kırmızı rengi beyaza diğer
    renkleri de siyaha dönüştüren program
"""
import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

lower_red = np.array([160, 100, 100])
upper_red = np.array([179, 255, 255])

while(video.isOpened()):
    ret, frame = video.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_red, upper_red)

    if ret:
        cv.imshow("kamera", mask)
        if cv.waitKey(33) == ord('q'):
            break