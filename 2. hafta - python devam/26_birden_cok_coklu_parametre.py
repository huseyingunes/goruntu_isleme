def hepsini_topla_carp(toplanacak, carpilacak):
    toplam = 0
    carpim = 1
    for i in toplanacak:
        toplam += i
    for i in carpilacak:
        carpim *= i
    return toplam, carpim


carpilacak_sayilar = [3, 5, 7]
print(hepsini_topla_carp([1, 5, 7, 9, 15, -5, 1.5], carpilacak_sayilar))
toplam, carpim = hepsini_topla_carp([1, 5, 7, 9, 15, -5, 1.5], carpilacak_sayilar)

print("Toplam : ", toplam)
print("Çarpım : ", carpim)
