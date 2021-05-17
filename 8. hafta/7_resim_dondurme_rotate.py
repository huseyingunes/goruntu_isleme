import cv2 as cv
import matplotlib.pyplot as plt

resim = cv.imread("resim/sudoku.jpg")

yeni_resim_1 = cv.rotate(resim, cv.ROTATE_90_CLOCKWISE)
yeni_resim_2 = cv.rotate(resim, cv.ROTATE_180)
yeni_resim_3 = cv.rotate(resim, cv.ROTATE_90_COUNTERCLOCKWISE)


titles = ['Gerçek', 'ROTATE_90_CLOCKWISE', 'ROTATE_180', 'ROTATE_90_COUNTERCLOCKWISE']
images = [resim, yeni_resim_1, yeni_resim_2, yeni_resim_3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()
