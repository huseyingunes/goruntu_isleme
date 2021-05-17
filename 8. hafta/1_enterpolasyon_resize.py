import cv2 as cv

resim = cv.imread("resim/bugday.jpg")

yeni_resim = cv.resize(resim, (300, 300))

cv.imshow("a", yeni_resim)
cv.waitKey(0)
