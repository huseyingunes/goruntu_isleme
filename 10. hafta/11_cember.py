import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

cv.circle(resim, (125, 150), 100, (20, 100, 50), 10, lineType=cv.LINE_AA)
cv.circle(resim, (350, 150), 100, (20, 100, 50), 10, lineType=cv.LINE_AA)
cv.circle(resim, (575, 150), 100, (20, 100, 50), 10, lineType=cv.LINE_AA)

cv.imshow("a", resim)
cv.waitKey(0)
