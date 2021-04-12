import numpy as np

dizi = np.array([10, 12, 14, 16])

#verilen elemanın dizi içindeki sırasını verir
bul = np.searchsorted(dizi, [11, 13, 15])

print(bul)
