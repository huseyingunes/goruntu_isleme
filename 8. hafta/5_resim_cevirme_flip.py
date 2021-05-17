import cv2 as cv

resim = cv.imread("resim/sudoku.jpg")

yeni_resim = cv.flip(resim, -1)

cv.imshow("a", yeni_resim)
cv.waitKey(0)
