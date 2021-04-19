import cv2 as cv

renkli = cv.imread("resim/manzara.jpg", cv.IMREAD_UNCHANGED)
saydam = cv.imread("resim/bilgisayar.png", cv.IMREAD_UNCHANGED)
gri = cv.imread("resim/manzara.jpg", cv.IMREAD_GRAYSCALE)
print(renkli.shape)
print(saydam.shape)
print(gri.shape)

cv.imshow("1", renkli)
cv.waitKey(3000)
cv.destroyWindow("1")

cv.imshow("2", saydam)
cv.waitKey(3000)
cv.destroyWindow("2")

cv.imshow("3", gri)
cv.waitKey(3000)
