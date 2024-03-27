import cv2 as cv
from PIL import ImageFont, Image, ImageDraw
import numpy as np

resim = cv.imread("resim/kirpilmis_manzara.jpg")
yazi_tipi_yolu = "yazitipi/Awesome Script Trial.otf"
yazi_tipi = ImageFont.truetype(yazi_tipi_yolu, 60)
img_pil = Image.fromarray(resim)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80),'Deneme', font=yazi_tipi)
img = np.array(img_pil)
cv.imshow("Türkçe yazı ve farklı yazıtipi kullanımı", img)

cv.waitKey(0)
