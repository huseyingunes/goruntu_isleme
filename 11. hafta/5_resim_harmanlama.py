import cv2 as cv

resim1 = cv.imread("resim/harman_1.png")
resim2 = cv.imread("resim/baun_logo.png")

sonuc = cv.addWeighted(resim1, .9, resim2, .1, 0)

cv.imshow("harman", sonuc)
cv.waitKey(0)