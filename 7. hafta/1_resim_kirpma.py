import cv2 as cv

resim = cv.imread("resim/bugday.jpg")

basak = resim[0:1024, 750:1024]

cv.imshow("a", basak)
cv.waitKey(0)

cv.imwrite("resim/kirpik_bugday.jpg", basak)

