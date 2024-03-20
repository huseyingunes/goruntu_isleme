"""
renk paleti oluşturun
"""

import cv2 as cv
import numpy as np

dizi = np.asarray(range(0, 196608)).reshape((256, 256, 3)).astype('uint8')

for i in range(256):
    for s in range(256):
        for d in range(256):
            dizi[i, s] = [i, s, d]

cv.imshow("", dizi)
cv.waitKey()
print(dizi)
