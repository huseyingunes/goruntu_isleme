import numpy as np

dizi = np.array([1, 2], ndmin=32)
print(dizi)
print("Dizinin boyutu:", dizi.ndim)

print("Bir dizi numpy de en fazla {} boyutlu olabilir.".format(32))