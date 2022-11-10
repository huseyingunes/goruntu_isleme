import numpy as np

dizi = np.asarray(range(1, 26)).reshape(5, 5)

kirmizi = dizi[:2, :2]
print(kirmizi)

yesil = dizi[:2, 3:]
print("yeşil :", yesil)

mavi = dizi[-2:, :2]
print("mavi :", mavi)

sari = dizi[-2:, -2:]
print(sari)


print(dizi)
