"""
4.1 deki örneği kameradan kendi yüzünüz için yapın.
kameranın sadece belirli bir noktasını kırpın ve bu efekti uygulayın.
"""

import cv2 as cv

video = cv.VideoCapture(0)
i=0
while(video.isOpened()):
    frame = video.read()[1]
    frame = frame[100:400, 200:700]
    satir, sutun = frame.shape[:2]
    #cv.imshow("frame", frame)
    i+=1
    M = cv.getRotationMatrix2D((sutun / 2, satir / 2), i, 0.5)
    sonuc = cv.warpAffine(frame, M, (sutun, satir), borderMode=cv.BORDER_REPLICATE)

    cv.imshow("sonuc", sonuc)

    if cv.waitKey(10) == ord('q'):
        break

quit()

    # cv.imshow("frame", frame)

resim = cv.imread("resim/manzara.jpg")

satir, sutun = resim.shape[:2]

print(satir, sutun)

while True:
    for i in range(360, 0, -1):
        M = cv.getRotationMatrix2D((sutun/2, satir/2), i, 0.5)
        sonuc = cv.warpAffine(resim, M, (sutun, satir), borderMode=cv.BORDER_REPLICATE)

        cv.imshow("sonuc", sonuc)
        cv.waitKey(10)


