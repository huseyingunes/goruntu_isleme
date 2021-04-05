import numpy as np

dizi = np.array([1, 2, 3])

x = dizi.copy()
y = dizi.view()

print(x.base)
print(y.base)
