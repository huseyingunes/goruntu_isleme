import cv2 as cv

resim = cv.imread("resim/b.tif", cv.IMREAD_UNCHANGED)

print(resim.shape)

resim[:, :, 2] = 0

cv.imshow("a", resim)
cv.waitKey(0)
