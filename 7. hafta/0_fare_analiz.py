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
    grayFrame = grayFrame[75:910, 430:1320]



    pts1 = np.float32([[74, 5], [860, 53], [40, 786], [806, 825]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    grayFrame = cv.warpPerspective(grayFrame, M, (500, 500))

    grayFrame = cv.medianBlur(grayFrame, 5)
    ret, esiklenmis = cv.threshold(grayFrame, 180, 255,
                                   cv.THRESH_BINARY)
    if ret:
        cv.imshow("fare takip", esiklenmis)
        if cv.waitKey(33) == 27:
            quit()