## 100*100 siyah bir resim oluşturun

import numpy as np
import cv2 as cv

resim = []
for a in range(0, 100):
    resim.append([])
    for b in range(0, 100):
        resim[a].append(0)
cv.imshow("", np.array(resim, dtype=np.uint8))
cv.waitKey(0)






liste = []
for x in range(0, 100):
    liste.append([])
    for y in range(0, 100):
        liste[x].append([])
        liste[x][y] = [0, y*2, 255-y*2]
liste = np.array(liste, dtype=np.uint8)
print(liste)
cv.imshow("", liste)
cv.waitKey(0)
