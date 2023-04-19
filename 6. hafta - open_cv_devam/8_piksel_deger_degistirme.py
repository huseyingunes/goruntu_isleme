import cv2 as cv

resim = cv.imread("resim/ad_soyad.jpg")
cv.imshow("a", resim)
cv.waitKey(0)
resim[10, 10] = [0, 0, 0]

print(resim[0, 0])

cv.imshow("a", resim)
cv.waitKey(0)

cv.imwrite("resim/ad_soyad_benekli.jpg", resim)

resim[10:50, 10:50] = [0, 0, 0]

print(resim[0, 0])

cv.imshow("a", resim)
cv.waitKey(0)

cv.imwrite("resim/ad_soyad_benekli_2.jpg", resim)
