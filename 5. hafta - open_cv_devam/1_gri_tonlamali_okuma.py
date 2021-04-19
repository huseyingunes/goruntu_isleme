import cv2 as cv

renkli = cv.imread("resim/manzara.jpg", cv.IMREAD_UNCHANGED)
saydam = cv.imread("resim/bilgisayar.png", cv.IMREAD_UNCHANGED)
gri = cv.imread("resim/manzara.jpg", cv.IMREAD_GRAYSCALE)
print(renkli.shape)
print(saydam.shape)
print(gri.shape)

cv.imshow("gri tonlamali resim", gri)
cv.waitKey(0)
