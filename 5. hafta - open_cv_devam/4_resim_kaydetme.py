import cv2 as cv

gri = cv.imread("resim/manzara.jpg", cv.IMREAD_GRAYSCALE)


cv.imwrite("resim/manzara_gri.jpg", gri)

manzara_gri = cv.imread("resim/manzara_gri.jpg")

cv.imshow("gri tonlamali resim", manzara_gri)
cv.waitKey(0)
