import cv2 as cv
import numpy as np
import tqdm

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("video/fare_analiz.avi", fourcc, 30.0, (500, 500))

video = cv.VideoCapture("video/F7of.mov")
i = 0

yesil_yol = []

total_frame = video.get(cv.CAP_PROP_FRAME_COUNT)
frame_no = 0

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
    grayFrame = cv.medianBlur(grayFrame, 5)

    ret, esiklenmis = cv.threshold(grayFrame, 180, 255,
                                   cv.THRESH_BINARY)

    x1,y1,x2,y2 = 1000,1000,0,0
    for i in range(esiklenmis.shape[0]):
        for j in range(esiklenmis.shape[1]):
            if esiklenmis[i][j] > 180:
                x1 = min (x1, j)
                y1 = min (y1, i)
                x2 = max (x2, j)
                y2 = max (y2, i)
    y = round((y1+y2)/2)
    x = round((x1+x2)/2)

    yesil_yol.append((x,y))

    renkli = cv.cvtColor(esiklenmis, cv.COLOR_GRAY2BGR)

    for s, yol in enumerate(yesil_yol):
        #renkli[yol[1] - 1:yol[1] + 1, yol[0] - 1:yol[0] + 1] = [0, 255, 0]
        if s > 0:
            cv.line(renkli, yesil_yol[s-1], yesil_yol[s], (0,255,0), 2)

    renkli[y - 3:y + 3, x - 3:x + 3] = [0, 0, 255]

    out.write(renkli)

    if ret:
        tqdm.tqdm(total=total_frame, initial=frame_no, desc="Fare Analiz", unit="frame")
        frame_no += 1
        #cv.imshow("fare takip", renkli)
        if cv.waitKey(33) == 27:
            out.release()
            quit()