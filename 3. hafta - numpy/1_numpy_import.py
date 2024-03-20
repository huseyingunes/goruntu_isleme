import numpy
import cv2

resim = cv2.imread("resim/python.png")
print(resim)
print(resim.shape)
print(type(resim))

cv2.imshow("asdf", resim)
cv2.waitKey(0)
