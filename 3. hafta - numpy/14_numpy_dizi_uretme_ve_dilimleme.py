import numpy as np

yeni_dizi = np.asarray(range(11, 36)).reshape(5, 5)

print(yeni_dizi)
print(yeni_dizi[0, 1:4])
print(yeni_dizi[1:4, 0])
print(yeni_dizi[::2, ::2])
print(yeni_dizi[:, 1])
