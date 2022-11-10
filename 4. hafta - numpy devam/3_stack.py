import numpy as np

dizi1 = np.array([1, 2, 3, 4])
dizi2 = np.array([4, 5, 6, 7])

yeni_dizi = np.stack((dizi1, dizi2))
print(yeni_dizi)

print("--------------------")
dizi1 = np.array([[1, 2], [3, 4]])
dizi2 = np.array([[4, 5], [6, 7]])

yeni_dizi, yeni_dizi2 = np.stack((dizi1, dizi2), axis=2)
print(yeni_dizi, yeni_dizi2)
