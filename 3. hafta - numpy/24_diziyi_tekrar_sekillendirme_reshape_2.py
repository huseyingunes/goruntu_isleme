import numpy as np

dizi = np.asarray(range(1, 101)).reshape((5, 5, 4))
print(dizi)

dizi = np.asarray(range(1, 251)).reshape((5, 5, -1))
print(dizi)
