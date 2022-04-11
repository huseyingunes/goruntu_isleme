import cv2 as cv
import numpy as np

dizi = np.zeros((256, 256), dtype="uint8")

for i in range(0, 255):
    dizi[:, i] = i

#cv.imwrite("resim/uretilmis.jpg", dizi)
#cv.imwrite("resim/uretilmis.bmp", dizi)
#cv.imwrite("resim/uretilmis.png", dizi)

uretilmis_resim = cv.imread("resim/uretilmis.jpg")
cv.imshow("1", uretilmis_resim)

while(True):
    tus = cv.waitKey(0)
    if tus == ord('j'):
        cv.imwrite("resim/uretilmis_tusla.jpg", dizi)
        break
    elif tus == ord('p'):
        cv.imwrite("resim/uretilmis_tusla.png", dizi)
        break
    elif tus == ord('t'):
        cv.imwrite("resim/uretilmis_tusla.tiff", dizi)
        break
    else:
        print("Hemşerim bir daha dene")
