import cv2 as cv
import numpy as np
smooth_x = None
smooth_y = None
alpha = 0.25   # 0.2 - 0.3 iyi başlangıç
video = cv.VideoCapture("video/F7of.mov")
i = 0
while video.isOpened():
    ret, frame = video.read()

    i += 1
    if i < 270:
        continue
    frame = frame[30:944, 421:1322]
    #frame = cv.resize(frame, (300, 300))
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.medianBlur(frame, 5)

    kernel = np.ones((5, 5), np.uint8)
    frame = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)

    ret2, frame = cv.threshold(frame, 180, 255, cv.THRESH_BINARY)
    x1, y1, x2, y2 = 0, 0, 0, 0
    for a in range(0, frame.shape[0], 5):
        for b in range(0, frame.shape[1], 5):
            #print(a, b)
            if frame[a][b] == 255:
                x2 = max(b, x2)
                y2 = max(a, y2)
                x1 = min(b, x1) if x1 != 0 else b
                y1 = min(a, y1) if y1 != 0 else a

    frame[y1:y1+2, x1:x2] = 123
    frame[y2-2:y2, x1:x2] = 123
    frame[y1:y2, x1:x1+2] = 123
    frame[y1:y2, x2-2:x2] = 123
    orta_x = round((x1+x2)/2)
    orta_y = round((y1+y2)/2)

    if smooth_x is None:
        smooth_x = orta_x
        smooth_y = orta_y
    else:
        smooth_x = int(alpha * orta_x + (1 - alpha) * smooth_x)
        smooth_y = int(alpha * orta_y + (1 - alpha) * smooth_y)

        # Kare çiz
    cv.rectangle(frame,
                  (smooth_x - 4, smooth_y - 4),
                  (smooth_x + 4, smooth_y + 4),
                  (123, 123, 123),
                  1)


    if ret:
        cv.imshow("Fare Analiz", frame)
        cv.waitKey(20)
    else:
        video.release()
        quit()