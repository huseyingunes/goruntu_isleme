import cv2 as cv

resim = cv.imread("resim/kirpik_bugday.jpg")

print(resim.shape)

print(resim[:, :, 0]) ## sadece mavi renk uzayını alır

cv.imshow("mavi", resim[:, :, 0])
cv.waitKey(0)
