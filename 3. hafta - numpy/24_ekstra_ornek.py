"""
Yukarıdan aşağıya beyazdan siyaha geçişli bir resim oluşturun
"""

import cv2 as cv
import numpy as np

dizi = np.asarray(range(0, 196608)).reshape((256, 256, 3)).astype('uint8')

for i in range(256):
    dizi[i, :] = [255-i, 255-i, 255-i]

cv.imshow("", dizi)
cv.waitKey()
print(dizi)
