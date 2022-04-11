import cv2 as cv

resim = cv.imread("resim/manzara.jpg")

print(resim.shape)
print(resim[0, 0])


for a in resim:
    for b in a:
        #print(b)
        b[2] = 0
        #b[1] = 0
        #b[0] = 0

cv.imshow("a", resim)
cv.waitKey(0)

