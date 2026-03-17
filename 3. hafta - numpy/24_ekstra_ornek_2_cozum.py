"""
renk paleti oluşturun
"""
import cv2
import numpy as np

genislik = 512
yukseklik = 512
red_degeri = 128

x = np.linspace(0, 255, genislik, dtype=np.uint8)
y = np.linspace(0, 255, yukseklik, dtype=np.uint8)

green_kanali = np.tile(x, (yukseklik, 1))
blue_kanali = np.tile(y.reshape(-1, 1), (1, genislik))
red_kanali = np.full((yukseklik, genislik), red_degeri, dtype=np.uint8)

palette = np.dstack((blue_kanali, green_kanali, red_kanali))

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = palette[y, x]
        print(f"Seçilen renk -> BGR: ({b}, {g}, {r})")

cv2.namedWindow("BGR Renk Paleti")
cv2.setMouseCallback("BGR Renk Paleti", mouse_callback)
cv2.imshow("BGR Renk Paleti", palette)
cv2.waitKey(0)
cv2.destroyAllWindows()