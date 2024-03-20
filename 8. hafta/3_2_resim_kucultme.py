# resim küçültme için alternatif yol
import cv2 as cv

resim = cv.imread("resim/bugday.jpg")

yeni_resim = resim[::4, ::4]

cv.imshow("a", yeni_resim)
cv.waitKey(0)
