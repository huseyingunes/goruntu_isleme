import cv2 as cv
import numpy as np

dizi = np.asarray(range(0, 30000)).reshape((100, 100, 3)).astype('int8')

cv.imshow("", dizi)
cv.waitKey()
print(dizi)