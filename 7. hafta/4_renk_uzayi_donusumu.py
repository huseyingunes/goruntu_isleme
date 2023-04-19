import cv2 as cv

resim = cv.imread("resim/b.tif", cv.IMREAD_UNCHANGED)
print(resim.shape)

gri = cv.cvtColor(resim, cv.COLOR_BGRA2GRAY)
print(gri.shape)

cv.imshow("a", gri)
cv.waitKey(0)
