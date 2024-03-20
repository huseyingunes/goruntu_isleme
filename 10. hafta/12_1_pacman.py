"""
elips çizerek pacman animasyonu yapınız.
İleri Düzey: Pacman sağa sola yukarı aşağı hareket edebilir (klavye tuşlarıyla)
"""

## Temel Çözüm

import cv2 as cv


resim = cv.imread("resim/kirpilmis_manzara.jpg")

i = 10
artis = 1

while True:
    kaynak = resim.copy()
    cv.ellipse(kaynak, (250, 150), (150, 150), 0, 10+i, 350-i, (255, 0, 0), -1)
    i += artis
    if i > 50 or i < 10:
        artis = artis * -1

    cv.imshow("", kaynak)
    cv.waitKey(10)