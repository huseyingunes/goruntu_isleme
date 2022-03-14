import numpy
import cv2

resim = cv2.imread("resim/python.png")
#print("resim dizisi boyutu :", resim.ndim)
print(resim)
resim[43:103, 65:105] = [255,0,0]
print(resim[43:103, 65:105])
print(type(resim))

cv2.imshow("asdf", resim)
cv2.waitKey(0)
