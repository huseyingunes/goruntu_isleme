import cv2 as cv

resim = cv.imread("resim/kirpik_bugday.jpg")

print(resim.shape)

print(resim[:, :, 0])  ## sadece mavi renk uzayını alır

cv.imshow("mavi", resim[:, :, 0])
cv.imshow("yesil", resim[:, :, 1])
cv.imshow("kirmizi", resim[:, :, 2])
cv.waitKey(0)
