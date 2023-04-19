import cv2 as cv
import time

bas_x = bas_y = 0
def fare_tiklama_olayi(event, x, y, flags, param):
    global bas_x, bas_y
    if event == cv.EVENT_LBUTTONDOWN:
        bas_x = x
        bas_y = y
        print("basıldı :", x, "-", y)

    if event == cv.EVENT_LBUTTONUP:
        print("bırakıldı :", x, "-", y)
        cv.imwrite("resim/kirpilmis_manzara_fare_ile.jpg", resim[bas_y:y, bas_x:x])
        cv.imshow("Kirpilmis Resim", resim[bas_y:y, bas_x:x])
        #cv.waitKey(0)
        #cv.destroyWindow("Kirpilmis Resim")

resim = cv.imread("resim/manzara.jpg")

cv.imshow("Fare", resim)
cv.setMouseCallback("Fare", fare_tiklama_olayi)
cv.waitKey(0)



