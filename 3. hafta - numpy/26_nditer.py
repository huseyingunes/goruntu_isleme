import numpy as np

dizi = np.asarray(range(1, 13)).reshape((1, 4, 3))
print(dizi)
'''
[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]]
'''
for eleman in np.nditer(dizi):
    print(eleman)

