import cv2
resim1 = cv2.imread('resim/harman_1.png')
resim2 = cv2.imread('resim/baun_logo.png')

rows, cols = resim2.shape[:2]
roi = resim1[:rows, :cols]

img2gray = cv2.cvtColor(resim2, cv2.COLOR_BGR2GRAY)
#cv2.imshow('result', img2gray)
#cv2.waitKey(0)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
#cv2.imshow('result', mask)
#cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('result', mask_inv)
#cv2.waitKey(0)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#cv2.imshow('result', img1_bg)
#cv2.waitKey(0)
dst = cv2.add(img1_bg, resim2)

cv2.imshow('result', dst)
cv2.waitKey(0)
