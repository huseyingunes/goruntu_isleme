# slat 23 de ki örnek
import numpy as np



dizi = np.asarray([(lambda x: range(x, x+6))(x) for x in range(0, 51, 10)])

print(dizi)

print("Kırmızı :", dizi[[0,2,5], 2])
print("Mavi :", dizi[3:, [0,2,5]])
print("Yeşil :", dizi[np.arange(5), np.arange(1, 6)])

