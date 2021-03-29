def hepsini_topla(*a):
    topla = 0
    for i in a:
        topla += i
    return topla

toplam = hepsini_topla(1,5,7,9,15,-5,1.5)

print("Toplam : ", toplam)
