## 100*100 siyah bir resim oluşturun

import numpy as np
import cv2 as cv

liste = []
for x in range(0, 100):
    liste.append([])
    for y in range(0, 100):
        liste[x].append([])
        liste[x][y] = [0, x*2, 255-x*2]
liste = np.array(liste, dtype=np.uint8)
print(liste)
cv.imshow("", liste)
cv.waitKey(0)
