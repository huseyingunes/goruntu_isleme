import numpy as np

dizi = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

yeni_dizi = np.array_split(dizi, 4)

print(yeni_dizi)
print(yeni_dizi[0])

