import numpy as np
# searchsorted doğru kullanılacaksa dizi önceden sıralanmalıdır.
dizi = np.array([8, 11, 9, 13, 12, 10])
dizi_harf = np.array(["a", "z", "r", "po", "pb"])

#verilen elemanın dizi içindeki sırasını verir
bul = np.searchsorted(dizi, 9)
print(bul)
bul2 = np.searchsorted(dizi_harf, "r")
print(bul2)


