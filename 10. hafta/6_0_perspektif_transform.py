import numpy as np
import cv2
resim = cv2.imread('resim/sudoku.jpg')
satir, sutun, kanal = resim.shape

print(satir, sutun)

kaynak_noktalar = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
hedef_noktalar = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(kaynak_noktalar, hedef_noktalar)
sonuc = cv2.warpPerspective(resim, M, (300, 300))

cv2.imshow("", sonuc)
cv2.waitKey(0)
