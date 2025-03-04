# 3 resmi 3 saniye aralıklarla arka arkaya göster
import cv2 as cv
import numpy as np

resimBmp = cv.imread("resim/resim.bmp")
resimPng = cv.imread("resim/resim.png")
resimJpg = cv.imread("resim/resim.jpg")


cv.imshow("BMP", resimBmp)
cv.waitKey(1500)
cv.destroyWindow("BMP")

cv.imshow("PNG", resimPng)
cv.waitKey(1500)
cv.destroyWindow("PNG")

cv.imshow("JPG", resimJpg)
cv.waitKey(1500)
cv.destroyWindow("JPG")