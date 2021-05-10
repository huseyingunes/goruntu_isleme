import cv2 as cv

resim = cv.imread("resim/b.tif", cv.IMREAD_UNCHANGED)

gri = cv.cvtColor(resim, cv.COLOR_BGR2GRAY)

cv.imshow("a", gri)
cv.waitKey(0)
