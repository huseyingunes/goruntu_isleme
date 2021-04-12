import numpy as np

dizi = np.array([10, 11, 12, 13, 14, 15])

#verilen elemanın dizi içindeki sırasını verir
bul = np.searchsorted(dizi, 12, side="right")

print(bul)
