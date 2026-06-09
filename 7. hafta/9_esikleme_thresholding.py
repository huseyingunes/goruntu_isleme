import cv2 as cv

resim = cv.imread("resim/sudoku.jpg", cv.IMREAD_GRAYSCALE)

ret, esiklenmis = cv.threshold(resim, 100, 255, cv.THRESH_BINARY)

cv.imshow("esiklenmis", esiklenmis)
cv.waitKey(0)
