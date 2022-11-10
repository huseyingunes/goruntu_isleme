'''
Örnek videoyu yavaştan hızlıya olacak şekilde,
yatay olarak aynalayarak gösteren
(en sağdaki piksellerin en sola gitmesi)
(flip kullanmadan)
ve
ESC tuşuna basıldığında video gösterimini sonlandıran
bir betik yazınız.
'''

import cv2 as cv
import numpy as np

video = cv.VideoCapture("video/ornek.mp4")

hiz = 100
hizlandirma_orani = 0

while (video.isOpened()):
    ret, frame = video.read()
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print(ret)
    frame2 = np.zeros((360, 640, 3), dtype="uint8")
    #print(frame.shape)
    for i in range(0, 640):
        frame2[:, i] = frame[:, 639-i]
    #quit()
    if ret:
        cv.imshow("video", frame2)
        if hiz > 10:
            hizlandirma_orani += 1
            if hizlandirma_orani % 2 == 0:
                hiz -= 1
        if cv.waitKey(hiz) == 27:
            break
