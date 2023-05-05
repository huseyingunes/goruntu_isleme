import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

cv.line(resim, (0, 0), (512, 256), (0, 255, 0), 10)

cv.imshow("a", resim)
cv.waitKey(0)
