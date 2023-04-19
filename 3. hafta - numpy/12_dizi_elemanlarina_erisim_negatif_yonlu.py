import numpy as np

a = np.array(15)
b = np.array([1, 2])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 22, 33, 44, 55], [66, 77, 88, 99, 100]]])

print("a dizisinin tek elemanı :", a)
print("b dizisinin 2. elemanı:", b[-1])
print("c dizisinin 2. elemanının 1. elemanı :", c[-1, -2])
print("d dizisinin 2. elemanının 1. elemanının 3. elemanı :", d[-1, -2, -3])

dizi = np.array(range(16))
yeni_dizi = np.array_split(dizi, 6)

print(yeni_dizi)