import cv2 as cv
import cv2

src = cv.imread("resim/bilgisayar.png", cv.IMREAD_UNCHANGED)
"""
cv.imshow() kullanırken gördüğünüz durum normaldir. 
Çünkü OpenCV pencere sistemi alpha (şeffaflık) 
kanalını desteklemez. Yani PNG’deki RGBA görüntü 
okunur ama gösterilirken alpha kanalı dikkate alınmaz.
"""
print("Seffaf Resim Boyutu :", src.shape)

cv.imshow("Baslik", src)
cv.waitKey(0)

print(src)

###################################################
### Alpha kanalını kullanarak şeffaf bir görüntüyü
### arka planla birleştirme
###################################################

import cv2 as cv
import numpy as np

src = cv.imread("resim/bilgisayar.png", cv.IMREAD_UNCHANGED)

bgr = src[:, :, :3]
alpha = src[:, :, 3] / 255.0

h, w = bgr.shape[:2]

background = np.ones((h, w, 3), dtype=np.uint8) * 255

for c in range(3):
    background[:,:,c] = bgr[:,:,c] * alpha + background[:,:,c] * (1 - alpha)

cv.imshow("image", background)
cv.waitKey(0)
