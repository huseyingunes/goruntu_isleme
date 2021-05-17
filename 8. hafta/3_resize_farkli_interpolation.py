import cv2 as cv
import matplotlib.pyplot as plt

resim = cv.imread("resim/sudoku.jpg")

yeni_resim_1 = cv.resize(resim, (2000, 2000), interpolation=cv.INTER_CUBIC)
yeni_resim_2 = cv.resize(resim, (2000, 2000), interpolation=cv.INTER_LINEAR)
yeni_resim_3 = cv.resize(resim, (2000, 2000), interpolation=cv.INTER_LANCZOS4)
yeni_resim_4 = cv.resize(resim, (2000, 2000), interpolation=cv.INTER_NEAREST)
yeni_resim_5 = cv.resize(resim, (2000, 2000), interpolation=cv.INTER_AREA)


titles = ['Gerçek', 'INTER_CUBIC', 'INTER_LINEAR', 'INTER_LANCZOS4', 'INTER_NEAREST', 'INTER_AREA']
images = [resim, yeni_resim_1, yeni_resim_2, yeni_resim_3, yeni_resim_4, yeni_resim_5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()