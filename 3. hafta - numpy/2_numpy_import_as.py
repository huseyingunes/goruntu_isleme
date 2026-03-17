import cv2 as cv
import numpy as np
import sys

python_listesi = [1, 2, 3, 4, 5]
dizi = np.array(python_listesi)

print(python_listesi)
print(dizi)
print(type(dizi))

python_listesi = [[1,2,3], [4,5,6], [128,129,130], [200,201,202], [250,253,255]]
resim = np.array(python_listesi, dtype=np.uint8)

cv.imshow("asdf", resim)
cv.waitKey(0)

print("Python listesi boyutu:", sys.getsizeof(python_listesi), "byte")
print("NumPy dizisi boyutu:", dizi.nbytes, "byte")

