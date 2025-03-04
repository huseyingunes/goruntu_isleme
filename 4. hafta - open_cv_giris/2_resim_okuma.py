import cv2 as cv

resim = cv.imread("resim/manzara.jpg")


cv.imshow("Manzara", resim)
cv.waitKey(0)

print(resim)
print(resim.shape)
print(resim.ndim)
