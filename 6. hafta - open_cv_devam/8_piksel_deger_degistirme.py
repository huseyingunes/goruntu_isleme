import cv2 as cv

resim = cv.imread("resim/ad_soyad.jpg")
cv.imshow("a", resim)
cv.waitKey(0)
resim[10, 10] = [0, 0, 0]

print(resim[0, 0])

cv.imshow("a", resim)
cv.waitKey(0)

cv.imwrite("resim/ad_syad,_benekli.jpg", resim)