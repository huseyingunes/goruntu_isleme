"""
Resim klasörünün altındaki test klasöründe bulunan 1024*1024 boyutundaki resimleri
test klasörünün altında ufak isminde bir klasör açarak
resimleri de 512*512 boyutuna getirerek aynı isimlerle kaydeden program
"""

import cv2 as cv
import os
import glob
from pathlib import Path












# İlk olarak ufak klasörünü test klasörü altında oluşturalım
yol = "resim/test/ufak"
if not os.path.isdir(yol):
   os.makedirs(yol)

# İkinci olarak klasörde bulunan bütün resimleri okuyabilmek
resimler = glob.glob("resim/test/*.jpg")
for resim in resimler:
   # Üçüncü olarak resimleri open cv ile okuyarak yeniden boyutlandırmamız gererkiyor
   ufaltilacak_resim = cv.imread(resim)
   yeniden_boyutlandirilmis_resim = cv.resize(ufaltilacak_resim, (512, 512), interpolation=cv.INTER_LANCZOS4)

   # Dördüncü olarak resmin sadece dosya ismini okumamız gerekiyor
   resim_adi = Path(resim).stem

   # Son olarak yeniden boyutlandırılmış resmi kaydediyoruz
   cv.imwrite("resim/test/ufak/"+resim_adi+".jpg", yeniden_boyutlandirilmis_resim)

   #cv.imshow("a", yeniden_boyutlandirilmis_resim)
   #cv.waitKey(500)
   print(resim)



