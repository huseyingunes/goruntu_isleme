import numpy as np

dizi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

suzgec = []
for i in range(1, 11):
    if i % 2 == 1:
        suzgec.append(True)
    else:
        suzgec.append(False)

print("Süzgeç Dizisi :", suzgec)
yeni_dizi = dizi[suzgec]

print(yeni_dizi)
