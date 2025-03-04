import cv2
import numpy as np

python_listesi = [1, 2, 3, 4, 5]
dizi = np.array(python_listesi)

print(python_listesi)
print(dizi)
print(type(dizi))

python_listesi = [[1,2,3], [4,5,6], [128,129,130], [200,201,202], [250,253,255]]
resim = np.array(python_listesi, dtype=np.uint8)

cv2.imshow("asdf", resim)
cv2.waitKey(0)

