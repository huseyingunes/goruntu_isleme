'''
Fare ile tıklatıldığında başlayıp bırakılan yerde biten ve çizgi çizen program.
Fare tıklandığı andan itibaren çizgi her zaman gözükmelidir.
-> Ödev : Fare Tıklatılırken CTRL basılı ise çizginin şekli farklı olsun.
'''
import cv2 as cv
from random import *

resim = cv.imread("resim/manzara.jpg")
temiz_resim = resim.copy()

fare_tiklatildi = False
baslangic_x = 0
baslangic_y = 0

def cizgi_ciz(event, x, y, flags, param):
    global fare_tiklatildi, baslangic_y, baslangic_x, resim, temiz_resim
    if event == cv.EVENT_LBUTTONDOWN:
        baslangic_x = x
        baslangic_y = y
        fare_tiklatildi = True

    if event == cv.EVENT_MOUSEMOVE:
        if fare_tiklatildi:
            resim = temiz_resim.copy()
            cv.line(resim, (baslangic_x, baslangic_y), (x, y), (255, 0, 0), 5)

    if event == cv.EVENT_LBUTTONUP:
        fare_tiklatildi = False




cv.namedWindow(winname="Resim")
cv.setMouseCallback("Resim", cizgi_ciz)

while True:
    cv.imshow("Resim", resim)
    if cv.waitKey(10) & 0xFF == 27:
        break

cv.destroyAllWindows()


