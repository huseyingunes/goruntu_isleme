"""
Yukarıdan aşağıya beyazdan siyaha geçişli
bir resim oluşturun
"""

import numpy as np
import cv2 as cv

resim = np.zeros((256, 256), dtype='uint8')

for i in range (256):
    resim[i, :] = [255-i]

cv.imshow("", resim)
cv.waitKey()














import cv2 as cv
import numpy as np

dizi = np.asarray(range(0, 256*256)).reshape((256, 256, 1)).astype('uint8')

for i in range(256):
    dizi[i, :] = [255-i]

cv.imshow("", dizi)
cv.waitKey()
print(dizi)
print(dizi.shape)
