import cv2 as cv
import numpy as np

video = cv.VideoCapture("video/gopro.mp4")

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        print("Okunamadi")
    else:
        cv.imshow("a", frame)
        cv.waitKey(5)
