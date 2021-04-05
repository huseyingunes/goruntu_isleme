import numpy as np

dizi = np.array([1, 2, 3])

yeni_dizi_goruntu = dizi
yeni_dizi_kopya = dizi.copy()

yeni_dizi_kopya[0] = 25
yeni_dizi_goruntu[1] = 36

print(dizi)
print(yeni_dizi_kopya)
print(yeni_dizi_goruntu)
