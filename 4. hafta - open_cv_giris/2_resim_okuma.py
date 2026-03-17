import cv2 as cv

resim = cv.imread("resim/manzara.jpg")
print(type(resim))
resim = resim[::2, ::2]
print("Shape :", resim.shape)

cv.imshow("Manzara", resim)
cv.waitKey(0)

print(resim)
print(resim.shape)
print(resim.ndim)
