import cv2 as cv

resim = cv.imread("resim/manzara.jpg")
cv.imshow("Baslik", resim)
cv.destroyWindow("Baslik")
cv.waitKey(3000)  # 3 saniye bekler sonra kapanır

print(resim)
