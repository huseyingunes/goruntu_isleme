import numpy as np

dizi = np.array([1123412, 2, 3], dtype="S")
dizi[0] = "123456789"
print("Dizi Veri Tipi :", dizi.dtype)
print("Dizi Veri Tipi :", dizi[0])

dizi = np.array(["1123412", "2", "3"], dtype="U")
print("Dizi Veri Tipi :", dizi.dtype)

dizi = np.array([1123412, 2, 3], dtype="f")
print("Dizi Veri Tipi :", dizi.dtype)
