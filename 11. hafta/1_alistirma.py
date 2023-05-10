'''
Resim üzerinde fare ile tıklanılan yere yuvarlak, dikdörtgen ya da rastgele boyutlarda elips çizen program.
'''
import cv2 as cv
from random import *

resim = cv.imread("resim/manzara.jpg")
yukseklik = resim.shape[0]
genislik = resim.shape[1]

def rastgele_sekil_ciz(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_RBUTTONDOWN:
        rastgele_islem = randint(1, 3)
        if rastgele_islem == 1:  # rastgele dikdörtgen çiz
            rastgele_uzunluk = randint(x, genislik)
            yarisi_x = int((rastgele_uzunluk - x) / 2)
            rastgele_yukseklik = randint(y, yukseklik)
            yarisi_y = int((rastgele_yukseklik - y) / 2)
            cv.rectangle(resim, (x-yarisi_x, y - yarisi_y),
                         (rastgele_uzunluk - yarisi_x, rastgele_yukseklik - yarisi_y),
                         (255, 100, 50), 10, lineType=cv.LINE_AA)
        elif rastgele_islem == 2:  # rastgele çember çiz
            kisa_mesafe = min(x, y, genislik - x, yukseklik - y)
            yaricap = randint(0, kisa_mesafe)
            cv.circle(resim, (x, y), yaricap, (20, 100, 50), 10, lineType=cv.LINE_AA)
        elif rastgele_islem == 3:  # rastgele elips çiz
            kisa_mesafe = min(x, y, genislik - x, yukseklik - y)
            yaricap = randint(0, kisa_mesafe)
            yaricap2 = randint(0, kisa_mesafe)
            cv.ellipse(resim, (x, y), (yaricap, yaricap2), 0, 0, 360, (255, 0, 0), -1)


cv.namedWindow(winname="Resim")
cv.setMouseCallback("Resim", rastgele_sekil_ciz)

while True:
    cv.imshow("Resim", resim)
    if cv.waitKey(10) & 0xFF == 27:
        break

cv.destroyAllWindows()


