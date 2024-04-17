import cv2 as cv

resim = cv.imread("resim/larva.jpg", cv.IMREAD_GRAYSCALE)

yuvarlaklar = cv.HoughCircles(resim, cv.HOUGH_GRADIENT, 1, 150,
                              param1=70, param2=5, minRadius=98, maxRadius=102)
renkli = cv.imread("resim/larva.jpg")
print(yuvarlaklar)



for cember in yuvarlaklar[0]:
    cv.circle(renkli, (int(cember[0]), int(cember[1])),
              int(cember[2]), (255, 0, 0), 1, lineType=cv.LINE_AA)

cv.imshow("a", renkli)
cv.waitKey(0)

