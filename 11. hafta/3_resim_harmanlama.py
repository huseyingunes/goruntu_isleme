import cv2 as cv

resim1 = cv.imread("resim/harman_1.png")
resim2 = cv.imread("resim/harman_2.png")

sonuc = cv.addWeighted(resim1, .2, resim2, .8, 0)

cv.imshow("harman", sonuc)
cv.waitKey(0)
