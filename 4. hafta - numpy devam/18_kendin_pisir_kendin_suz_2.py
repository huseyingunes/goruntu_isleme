import numpy as np

dizi = np.array([21, 2, 3, 4, 5, 6, 7, 8, 9, 10])

suzgec = dizi % 2 == 1

yeni_dizi = dizi[suzgec]

print("Süzgeç :", suzgec)
print(yeni_dizi)
