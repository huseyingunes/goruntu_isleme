import cv2 as cv

resim = cv.imread("resim/fotografci.png")

yumusatilmis_resim = cv.GaussianBlur(resim, (5, 5), 1)

cv.imshow("a", yumusatilmis_resim)
cv.waitKey(0)
