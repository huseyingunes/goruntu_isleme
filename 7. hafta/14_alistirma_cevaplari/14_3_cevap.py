"""
3 - Resmin istenilen bir bölgesini, farklı bir resmin aynı
    bölgesi ile değiştiren program
"""

import cv2 as cv


resim_sudoku = cv.imread("../resim/sudoku.jpg")
resim_bugday = cv.imread("../resim/bugday.jpg")

resim_bugday[50:400, 50:200] = resim_sudoku[50:400, 50:200]

cv.imshow("kirpilmis resim", resim_bugday)
cv.waitKey(0)