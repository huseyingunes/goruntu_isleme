import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

cv.ellipse(resim, (200, 200), (200, 50), 0, 100, 270, (255, 0, 0), -1)

cv.imshow("a", resim)
cv.waitKey(0)
