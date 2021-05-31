import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

cv.rectangle(resim, (50, 50), (500, 250), (255, 100, 50), 10, lineType=cv.LINE_AA)

cv.imshow("a", resim)
cv.waitKey(0)
