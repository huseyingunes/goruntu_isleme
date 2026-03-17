import numpy as np

dizi = np.array([4, 1, 2, 3, 4, 5, 6, 4, 7, 4])
#çift sayıları bulma
#a = dizi % 2 == 0
#print("a nın tipi :", type(a))
bul = np.where(dizi % 2 == 0)

print(bul)
