import cv2 as cv

resim = cv.imread("resim/seffaf_olacak.jpg", cv.IMREAD_UNCHANGED)
resim_gri = cv.imread("resim/seffaf_olacak.jpg", cv.IMREAD_GRAYSCALE)
seffaf = cv.cvtColor(resim, cv.COLOR_BGR2BGRA)

'''
## şeffaf olan piksellerin alpha kanal değerini okumak için yazdık
resim_seffaf = cv.imread("resim/seffaf_photoshop_saydam.png", cv.IMREAD_UNCHANGED)
print(resim_seffaf.shape)
print(resim_seffaf[:, :, 3])
quit()
'''

for x in range(0, 480):
    for y in range(0, 640):
        if (resim_gri[x, y] >= 200):
            seffaf[x, y, 3] = 0


cv.imshow("a", seffaf)
cv.waitKey(0)
cv.imwrite("resim/a_alpha_kanalli.png", seffaf)

