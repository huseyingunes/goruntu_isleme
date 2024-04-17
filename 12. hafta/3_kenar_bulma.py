import cv2 as cv

resim = cv.imread("resim/ronaldo.jpg")

resim = cv.resize(resim, (500, 750))
kenarlar = cv.Canny(resim, threshold1=200, threshold2=200)

cv.imshow("a", kenarlar)
cv.waitKey(0)
