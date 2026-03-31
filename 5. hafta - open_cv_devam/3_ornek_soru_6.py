"""
Satranç tahtasını oluşturunuz.
Tahtanın beyaz karelerinin yukarıdan
aşağı aktığını düşününüz.
Bu beyaz karelerinin yukarıdan random
sırayla gelmesini sağlayınız.
"""


import cv2 as cv
import numpy as np
import random

chess_board = np.zeros((8*64, 8*64, 3), dtype=np.uint8)

manzara = cv.imread("resim/manzara.jpg")

white_cells = []

# Beyaz kareleri listeye al
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            white_cells.append((i, j))

# Listeyi karıştır
random.shuffle(white_cells)

# Random sırayla oluştur
for (i, j) in white_cells:

    x = random.randint(0, manzara.shape[0] - 64)
    y = random.randint(0, manzara.shape[1] - 64)

    top_left = (i * 64, j * 64)
    bottom_right = ((i + 1) * 64, (j + 1) * 64)

    selected_area = manzara[x:x + 64, y:y + 64]

    selected_area_resized = cv.resize(
        selected_area,
        (bottom_right[1] - top_left[1], bottom_right[0] - top_left[0])
    )

    chess_board[top_left[0]:bottom_right[0],
                top_left[1]:bottom_right[1]] = selected_area_resized

    cv.imshow("Chess Board", chess_board)
    cv.waitKey(100)

cv.waitKey(0)