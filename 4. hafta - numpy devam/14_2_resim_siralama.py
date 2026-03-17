import cv2 as cv
import numpy as np

resim = cv.imread("resim/manzara.jpg", cv.IMREAD_GRAYSCALE)
resim = cv.imread("resim/manzara.jpg")

yeni_dizi = np.sort(resim)
print(yeni_dizi)

cv.imshow("asc", yeni_dizi)
cv.waitKey(0)

print(yeni_dizi)