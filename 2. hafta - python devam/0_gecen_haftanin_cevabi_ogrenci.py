"""
Mustafa Koray Memiş
1 - Klavyeden girilen 5 tane sayıyı bir listeye atayarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
    ipucu : x = eval(input())
"""
sayilar = []
for i in range(5):
  sayi = eval(input("{}. sayıyı girin: ".format(i+1)))
  sayilar.append(sayi)

sonuclar = []
for sayi in sayilar:
  kare = sayi**2
  fark = kare - 20
  sonuclar.append(fark)

sirali = sorted(zip(sonuclar, sayilar))
print(sirali)

'''
-5,   3, 10,   1,  7
 5, -11, 80, -19, 29
 1, 3, -5, 7, 10
'''
