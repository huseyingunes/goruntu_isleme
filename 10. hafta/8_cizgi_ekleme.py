import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

cv.line(resim, (0, 0), (256, 256), (255, 0, 0), 5)

cv.imshow("a", resim)
cv.waitKey(0)
