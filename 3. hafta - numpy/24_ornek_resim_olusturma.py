import cv2 as cv
import numpy as np

dizi = np.asarray(range(0, 750000)).reshape((500, 500, 3)).astype('int8')

cv.imshow("", dizi)
cv.waitKey()
print(dizi)
