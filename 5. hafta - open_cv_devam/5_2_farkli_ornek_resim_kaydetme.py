import cv2 as cv
import numpy as np

dizi = np.zeros((512, 512), dtype="uint8")

for i in range(0, 256):
    dizi[:256, i] = i
    dizi[:256, -i] = i
dizi[0:256, 256] = 255

for i in range(256, 512):
    dizi[256:512, i] = i
    dizi[256:512, -i] = i

cv.imwrite("resim/uretilmis.jpg", dizi)

uretilmis_resim = cv.imread("resim/uretilmis.jpg")
cv.imshow("1", uretilmis_resim)
cv.waitKey(0)





