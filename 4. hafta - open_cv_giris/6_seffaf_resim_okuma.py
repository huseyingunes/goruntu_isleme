import cv2 as cv
import cv2

src = cv.imread("resim/bilgisayar.png", cv.IMREAD_UNCHANGED)

print("Seffaf Resim Boyutu :", src.shape)

*_, alpha = cv2.split(src)

gray_layer = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

dst = cv2.merge((gray_layer, gray_layer, gray_layer, alpha))

cv.imshow("Baslik", dst)
cv.waitKey(0)

print(src)
