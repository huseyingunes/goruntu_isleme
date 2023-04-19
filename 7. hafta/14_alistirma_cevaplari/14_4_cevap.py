"""
4 - Kameradan alınan görüntüyü görüntünün ortanca değerine
    göre siyah beyaza dönüştüren program
"""
import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ortalama = np.average(grayFrame)
    ret, esiklenmis = cv.threshold(grayFrame, ortalama, 255,
                                   cv.THRESH_BINARY)

    if ret:
        cv.imshow("kamera", esiklenmis)
        if cv.waitKey(33) == ord('q'):
            break