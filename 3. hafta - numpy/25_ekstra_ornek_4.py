"""
copilot a yaptır
paintteki gibi renk paleti oluşturun
"""
import cv2 as cv
import numpy as np

# Create an empty 256x256 HSV image
image = np.zeros((256, 256, 3), dtype=np.uint8)

# Fill the image with HSV values.
# Hue is set using the column index (s), Saturation using an inversion of the row index (255 - i), and Value is constant at 255.
for i in range(256):
    for s in range(256):
        image[i, s] = [s, 255 - i, 255]

# Convert the HSV image to BGR for displaying using OpenCV.
bgr_image = cv.cvtColor(image, cv.COLOR_HSV2BGR)

cv.imshow("Palette", bgr_image)
cv.waitKey(0)
cv.destroyAllWindows()