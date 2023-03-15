import numpy as np

dizi = np.array([1, 2, 3])
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array([1.0, 2.2, 3.3])
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array(["1", "2", "3"])
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array(["111", "222", "3334"])
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array([111111111111, 2, 3])
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array([11111111234523452345, 2, 3])
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array([11111111234523452345244, 2, 3])
print("Dizi Veri Tipi :", dizi.dtype)

print("----------------------------------------")

dizi = np.array([1, 2, 3])
print("Dizi Veri Tipi :", dizi.dtype)
#dizi[0] = 11111111234
print("Dizi Veri Tipi :", dizi.dtype)
dizi = np.append(dizi, 11111111234)
print("Dizi Veri Tipi :", dizi.dtype)
print(dizi)
print("Dizi Veri Tipi :", dizi.dtype)
