"""
6_0 örneğinde sudoku resminin perspektifi düzeltilmesine rağmen ufak hatalar kalmıştır.
Sudoku resminde üst tarafta yer alan yamukluğu da düzeltiniz.
"""
import numpy as np
import cv2
resim = cv2.imread('resim/sudoku.jpg')
satir, sutun, kanal = resim.shape

print(satir, sutun)

kaynak_noktalar = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
hedef_noktalar = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(kaynak_noktalar, hedef_noktalar)
sonuc = cv2.warpPerspective(resim, M, (300, 300))

cv2.imwrite("resim/sudoku_perspektif_duzeltilmis.jpg", sonuc)


sol_taraf = sonuc[:, 0:201]
kaynak_noktalar = np.float32([[0, 0], [200, 8], [0, 300], [200, 300]])
hedef_noktalar = np.float32([[0, 0], [200, 0], [0, 300], [200, 300]])
M = cv2.getPerspectiveTransform(kaynak_noktalar, hedef_noktalar)
sonuc_sol_taraf = cv2.warpPerspective(sol_taraf, M, (200, 300))

sag_taraf = sonuc[:, 201:]
kaynak_noktalar = np.float32([[0, 8], [100, 0], [0, 300], [100, 300]])
hedef_noktalar = np.float32([[0, 0], [100, 0], [0, 300], [100, 300]])
M = cv2.getPerspectiveTransform(kaynak_noktalar, hedef_noktalar)
sonuc_sag_taraf = cv2.warpPerspective(sag_taraf, M, (100, 300))

son = cv2.hconcat([sonuc_sol_taraf, sonuc_sag_taraf])

cv2.imshow("", son)

cv2.waitKey(0)

