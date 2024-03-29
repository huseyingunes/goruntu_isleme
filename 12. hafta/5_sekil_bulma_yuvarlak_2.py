import cv2 as cv

resim = cv.imread("resim/larva.jpg", cv.IMREAD_GRAYSCALE)

yuvarlaklar = cv.HoughCircles(resim, cv.HOUGH_GRADIENT, 1, 1, param1=60, param2=20, minRadius=95, maxRadius=108)
renkli = cv.imread("resim/larva.jpg")

for cember in yuvarlaklar[0]:
    cv.circle(renkli, (int(cember[0]), int(cember[1])), int(cember[2]), (255, 0, 0), 1, lineType=cv.LINE_AA)

cv.imshow("a", renkli)
cv.waitKey(0)

