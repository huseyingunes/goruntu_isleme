def benim_fonksiyonum(n):
  return lambda a: a * n


katini_al = benim_fonksiyonum(2)
print(katini_al(5))

katini_al = benim_fonksiyonum(5)
print(katini_al(5))

