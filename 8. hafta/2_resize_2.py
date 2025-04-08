import cv2 as cv

resim = cv.imread("resim/sudoku.jpg")

yeni_resim = cv.resize(resim, (2000, 2000), interpolation=cv.INTER_CUBIC)

cv.imwrite("resim/sudoku_2000_2000.jpg", yeni_resim)

cv.imshow("a", yeni_resim)
cv.waitKey(0)
