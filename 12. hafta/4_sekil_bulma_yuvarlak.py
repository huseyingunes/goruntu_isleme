import cv2 as cv

resim = cv.imread("resim/ronaldo_2.jpg", cv.IMREAD_GRAYSCALE)

yuvarlaklar = cv.HoughCircles(resim, cv.HOUGH_GRADIENT, 1, 1, param1=100, param2=30, minRadius=30, maxRadius=50)
renkli = cv.imread("resim/ronaldo_2.jpg")

for cember in yuvarlaklar[0]:
    cv.circle(renkli, (cember[0], cember[1]), int(cember[2]), (255, 0, 0), 1)

cv.imshow("a", renkli)
cv.waitKey(0)


