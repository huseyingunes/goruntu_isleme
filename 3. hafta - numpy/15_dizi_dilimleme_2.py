import numpy as np

yeni_dizi = np.asarray(range(0, 36)).reshape(6, 6)

print(yeni_dizi)
print(yeni_dizi[0, 3:5])
print(yeni_dizi[:, 2])
print(yeni_dizi[-2:, -2:])

print(yeni_dizi[2::2, ::2])

