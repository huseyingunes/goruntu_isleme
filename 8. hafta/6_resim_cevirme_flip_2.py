import cv2 as cv
import matplotlib.pyplot as plt

resim = cv.imread("resim/sudoku.jpg")

yeni_resim_1 = cv.flip(resim, -1)
yeni_resim_2 = cv.flip(resim, 0)
yeni_resim_3 = cv.flip(resim, 1)


titles = ['Gerçek', '-1', '0', '1']
images = [resim, yeni_resim_1, yeni_resim_2, yeni_resim_3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()