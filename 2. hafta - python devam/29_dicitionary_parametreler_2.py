def birim_islem(**birim):
  print("Birimin tipi:", type(birim))
  for a, b in birim.items():
    print(a, ":", b)


birim_islem(ad="Balıkesir", tip="Üniversite", yil=1992, renk="yeşil")
