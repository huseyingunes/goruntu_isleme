import numpy as np
import cv2
resim = cv2.imread('resim/dosya.jpg')
satir, sutun, kanal = resim.shape

print(satir, sutun)

kaynak_noktalar = np.float32([[435, 124], [997, 323], [34, 700], [692, 984]])
hedef_noktalar = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])

M = cv2.getPerspectiveTransform(kaynak_noktalar, hedef_noktalar)
sonuc = cv2.warpPerspective(resim, M, (600, 600))

cv2.imshow("", sonuc)
cv2.waitKey(0)
