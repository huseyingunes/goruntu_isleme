import cv2 as cv
import pyautogui
import numpy as np

img = pyautogui.screenshot()
img = np.array(img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imwrite("ekran.jpg", img)
