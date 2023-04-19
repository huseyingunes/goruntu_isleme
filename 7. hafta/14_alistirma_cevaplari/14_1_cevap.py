"""
1 - Parametre olarak verilen x1,y1 ve x2,y2 değerlerine
    göre resmi kırpan fonksiyon
"""
import cv2 as cv

def resim_kirp(resim, x1, y1, x2, y2):
    return resim[y1:y2, x1:x2]

resim = cv.imread("../resim/sudoku.jpg")
kirpilmis_resim = resim_kirp(resim, 100, 100, 300, 400)
cv.imshow("kirpilmis resim", kirpilmis_resim)
cv.waitKey(0)
