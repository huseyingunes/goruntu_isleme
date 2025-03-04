# slat 22 de ki örnek
import numpy as np



dizi = np.asarray([(lambda x: range(x, x+6))(x) for x in range(0, 51, 10)])

print(dizi)

print("Kırmızı :", dizi[0, 3:5])
print("Mavi :", dizi[:, 2])
print("Yeşil :", dizi[-2:, -2:])
print("Mor :", dizi[2::2, ::2])
