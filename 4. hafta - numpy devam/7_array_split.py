import numpy as np

dizi = np.array([1, 2, 3, 4, 5, 6])

yeni_dizi = np.array_split(dizi, 3)

print(yeni_dizi)
print(yeni_dizi[0])
