import cv2 as cv
import numpy as np

resim = cv.imread("resim/kirpilmis_manzara.jpg")

line1 = np.array([[100, 20],  [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [300, 100]], np.int32).reshape((-1, 1, 2))
cv.polylines(resim, [line1, line2, line3], True, (0, 255, 255))


cv.imshow("a", resim)
cv.waitKey(0)
