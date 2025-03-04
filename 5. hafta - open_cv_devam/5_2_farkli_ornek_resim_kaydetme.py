import cv2 as cv
import numpy as np

dizi = np.zeros((512, 512), dtype="uint8")


for i in range(0, 256):
    dizi[i, :256] = i
    dizi[-i, :256] = i
dizi[256, 0:256] = 255


for i in range(0, 256):
    dizi[i, 256:512] = i
    dizi[-i, 256:512] = i
dizi[256, 256:512] = 255

cv.imwrite("resim/uretilmis.jpg", dizi)

uretilmis_resim = cv.imread("resim/uretilmis.jpg")
cv.imshow("1", uretilmis_resim)
cv.waitKey(0)





