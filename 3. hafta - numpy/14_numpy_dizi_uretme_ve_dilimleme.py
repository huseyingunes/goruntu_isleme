import numpy as np

yeni_dizi = np.asarray(range(11, 36)).reshape(5, 5)

print(yeni_dizi)
print(yeni_dizi[0, 1:4])
print(yeni_dizi[1:4, 0])
print(yeni_dizi[::2, ::2])
print(yeni_dizi[:, 1])


yeni_dizi = np.asarray([0] * 10000, dtype="uint8").reshape(100, 100)
#yeni_dizi = np.asarray(range(0, 1), dtype="uint8").repeat(10000).reshape(100, 100)
import cv2 as cv
cv.imshow("sdf", yeni_dizi)
cv.waitKey(0)