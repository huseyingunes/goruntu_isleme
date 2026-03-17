import numpy as np

dizi = np.array([1, 2, 3, 4, 5, 6])
print(type(dizi))
yeni_dizi = np.array_split(dizi, 5)

print(yeni_dizi)
print(type(yeni_dizi))
print(type(yeni_dizi[0]))
print(yeni_dizi[0])
