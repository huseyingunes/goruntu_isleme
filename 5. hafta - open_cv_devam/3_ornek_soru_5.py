"""
Bir önceki satranç tahtasına benzer bir tahta oluşturunuz.
Bu sefer tahtanın her bir beyaz karesine manzara resmini yerleştiriniz.
Manzarar resminin rastgele 100*100 lük kısmını kullanınız.
"""

import cv2 as cv
import numpy as np
import random

dizi = np.zeros((800, 800, 3), dtype="uint8")

manzara = cv.imread("resim/manzara.jpg")




for i in range(0, 8):
    for s in range(0, 8):
        x = random.randint(0, manzara.shape[0] - 100)
        y = random.randint(0, manzara.shape[1] - 100)
        if (i+s)%2 == 0:
            dizi[i*100:i*100+100, s*100:s*100+100] = manzara[x:x+100, y:y+100]



cv.imshow("1", dizi)
#cv.imwrite("resim/satranc_manzara.bmp", dizi)
cv.waitKey(0)