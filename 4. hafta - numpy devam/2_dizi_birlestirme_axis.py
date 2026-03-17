import numpy as np

dizi1 = np.array([[1, 2], [3, 4]])
dizi2 = np.array([[5, 6], [7, 8]])

yeni_dizi = np.concatenate((dizi1, dizi2), axis=0)

print(yeni_dizi)

yeni_dizi = np.concatenate((dizi1, dizi2), axis=1)

print(yeni_dizi)
