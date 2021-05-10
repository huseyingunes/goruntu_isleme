import cv2 as cv

resim = cv.imread("resim/a.png", cv.IMREAD_UNCHANGED)

print(resim.shape)
seffaf = cv.cvtColor(resim, cv.COLOR_BGR2BGRA)
print(seffaf.shape)
cv.imshow("a", seffaf)
cv.waitKey(0)
cv.imwrite("resim/a_alpha_kanalli.png", seffaf)

