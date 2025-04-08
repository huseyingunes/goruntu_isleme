import cv2 as cv

resim = cv.imread("resim/manzara.jpg")

satir, sutun = resim.shape[:2]

print(satir, sutun)

M = cv.getRotationMatrix2D((sutun/2, satir/2), 45, 0.25)
sonuc = cv.warpAffine(resim, M, (int(sutun), int(satir)), borderMode=cv.BORDER_REPLICATE)


cv.imshow("sonuc", sonuc)
cv.waitKey(0)
