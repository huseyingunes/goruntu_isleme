'''
1 - Affin dönüşümünü kameradan alınan görütüde dene.
    Reflecti de uygula
2 - Kameradan görüntüyü alarak sürekli olarak çeviren
    Replicative uygulayan bir uygulama
'''


import cv2 as cv

kamera = cv.VideoCapture(0)
ret, resim = kamera.read()
satir, sutun = resim.shape[:2]

while True:
    for i in range(360, 0, -1):
        ret, resim = kamera.read()
        M = cv.getRotationMatrix2D((sutun/2, satir/2), i, 0.5)
        sonuc = cv.warpAffine(resim, M, (sutun, satir), borderMode=cv.BORDER_REPLICATE)

        cv.imshow("sonuc", sonuc)
        cv.waitKey(33)


