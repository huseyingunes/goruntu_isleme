## BORDER_REPLICATE kullanarak
## resminizi 0 dan 360 dereceye döndüren bir program yazınız.
## döndürme noktası resmin merkezi olsun.
## resim döndürülürken hiçbir tarafı kırpılmasın.
#resim sürekli ve saat yönünde döndürülsün.







import cv2 as cv

resim = cv.imread("resim/manzara.jpg")

satir, sutun = resim.shape[:2]

print(satir, sutun)

while True:
    for i in range(360, 0, -1):
        M = cv.getRotationMatrix2D((sutun/2, satir/2), i, 0.5)
        sonuc = cv.warpAffine(resim, M, (sutun, satir), borderMode=cv.BORDER_REPLICATE)

        cv.imshow("sonuc", sonuc)
        cv.waitKey(10)


