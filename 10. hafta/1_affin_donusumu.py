import cv2 as cv

resim = cv.imread("resim/manzara.jpg")

satir, sutun = resim.shape[:2]

print(satir, sutun)

M = cv.getRotationMatrix2D((sutun/2, satir/2), -45, .5)

sonuc = cv.warpAffine(resim, M, (int(sutun*2), int(satir*2)))

cv.imshow("sonuc", sonuc)
cv.waitKey(0)
