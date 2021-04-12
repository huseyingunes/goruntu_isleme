import cv2 as cv

resim = cv.imread("resim/manzara.jpg", cv.IMREAD_GRAYSCALE)

cv.imshow("Baslik", resim)
cv.waitKey(0)

print(resim)
