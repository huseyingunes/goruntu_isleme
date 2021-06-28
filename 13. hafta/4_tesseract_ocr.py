import cv2
import pytesseract

img_cv = cv2.imread("resim/metin.jpg")

img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img_rgb, lang="tur"))
