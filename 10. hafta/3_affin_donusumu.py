import cv2 as cv

resim = cv.imread("resim/sudoku.jpg")

satir, sutun = resim.shape[:2]

print(satir, sutun)

M = cv.getRotationMatrix2D((sutun/2, satir/2), 45, 0.5)
sonuc = cv.warpAffine(resim, M, (sutun, satir), borderMode=cv.BORDER_REFLECT101)


cv.imshow("sonuc", sonuc)
cv.waitKey(0)
