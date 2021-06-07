import cv2
resim1 = cv2.imread('resim/harman_1.png')
resim2 = cv2.imread('resim/sudoku.jpg')

rows, cols = resim2.shape[:2]
roi = resim1[:rows, :cols]

img2gray = cv2.cvtColor(resim2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, resim2)
resim1[:rows, :cols] = dst

cv2.imshow('result', resim1)
cv2.waitKey(0)
