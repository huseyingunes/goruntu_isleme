from random import randrange, shuffle
from random import randrange as rastgele

print(randrange(1, 10))

x = randrange(10, 100)
print(x)


print(rastgele(1, 10))

x = rastgele(10, 100)
print(x)

##############################################
x = [1, 3, 5, 7, 9]
shuffle(x)
print(x)
