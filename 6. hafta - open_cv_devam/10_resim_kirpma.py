import cv2 as cv

resim = cv.imread("resim/manzara.jpg")

print(resim.shape)
#600,500 den 900,1200
yol = resim[600:900, 500:1200]
print(yol)
cv.imshow("a", yol)
cv.waitKey(0)

cv.imwrite("resim/kirpilmis_manzara.jpg", yol)

