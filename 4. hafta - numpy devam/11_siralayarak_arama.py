import numpy as np

dizi = np.array([15, 11, 9, 13, 12, 10])
dizi_harf = np.array(["a", "z", "r", "po", "pb", "pa"])

#verilen elemanın dizi içindeki sırasını verir
bul = np.searchsorted(dizi, 12)
print(bul)

bul2 = np.searchsorted(dizi_harf, "r")
print(bul2)


