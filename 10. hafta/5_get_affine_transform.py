import cv2 as cv
import numpy as np

resim = cv.imread("resim/manzara.jpg")

satir, sutun = resim.shape[:2]

kaynak_noktalar = np.float32([[0, 0], [sutun-1, 0], [0, satir-1]])
hedef_noktalar = np.float32([[0, 0], [int(0.6*(sutun-1)), 0], [int(0.4*(sutun-1)), satir-1]])
afin_matrisi = cv.getAffineTransform(kaynak_noktalar, hedef_noktalar)
sonuc = cv.warpAffine(resim, afin_matrisi, (sutun, satir))

cv.imshow("sonuc", sonuc)
cv.waitKey(0)
