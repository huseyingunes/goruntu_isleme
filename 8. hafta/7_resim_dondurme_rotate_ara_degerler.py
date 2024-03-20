import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

resim = cv.imread("resim/sudoku.jpg")

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
  return result

yeni_resim_1 = rotate_image(resim, 45)
yeni_resim_2 = rotate_image(resim, 135)
yeni_resim_3 = rotate_image(resim, 215)


titles = ['Gerçek', 'ROTATE_90_CLOCKWISE', 'ROTATE_180', 'ROTATE_90_COUNTERCLOCKWISE']
images = [resim, yeni_resim_1, yeni_resim_2, yeni_resim_3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()
