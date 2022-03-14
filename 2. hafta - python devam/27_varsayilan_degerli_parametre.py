def ussunu_al(sayi, us_degeri=2):
    ussu = 1
    for i in range(us_degeri):
        ussu *= sayi
    return ussu


print("2 üzeri 2 :", ussunu_al(2))
print("2 üzeri 8 :", ussunu_al(2, 8))
