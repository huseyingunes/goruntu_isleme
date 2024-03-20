import cv2 as cv

resim = cv.imread("resim/manzara.jpg")
cv.imshow("kirpilmamis", resim)
cv.waitKey(0)
print(resim.shape)
#600,500 den 900,1200
yol = resim[600:900, 500:1200]
print(yol)
cv.imshow("a", yol)
cv.waitKey(0)

cv.imwrite("resim/kirpilmis_manzara.jpg", yol)

cali = resim[500:750, 200:430]
print(cali)
cv.imshow("a", cali)
cv.waitKey(0)
