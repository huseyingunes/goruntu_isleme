'''
Maviden kırmızıya 256*256 piksellik bir resim oluşturun
ve opencv imshow ile gösterin
'''

import cv2 as cv
import numpy as np







dizi = np.zeros((256, 256, 3), dtype="uint8")
print(dizi.shape)
print(dizi.ndim)
print(dizi.dtype)
print(dizi)
for i in range(0, 255):
    dizi[:, i] = [255-i, 0, i]

print(dizi)

cv.imshow("1", dizi)
cv.waitKey(0)





