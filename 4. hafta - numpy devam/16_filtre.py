import numpy as np

dizi = np.array([1, 2, 3, 4])

suzgec = [True, False, True, False]

yeni_dizi = dizi[suzgec]
yeni_dizi_2 = np.where(dizi % 2 == 1)

print(yeni_dizi)
print(yeni_dizi_2)
