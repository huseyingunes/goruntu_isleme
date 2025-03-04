"""
paintteki gibi renk paleti oluşturun
"""

import cv2 as cv
import numpy as np

dizi = np.asarray(range(0, 256*256*3)).reshape((256, 256, 3)).astype('uint8')

for i in range(256):
    for s in range(256):
            dizi[i, s] = [s, 255-i, 255]

bgr_image = cv.cvtColor(dizi, cv.COLOR_HSV2BGR)

cv.imshow("", bgr_image)
cv.waitKey()
print(bgr_image)
