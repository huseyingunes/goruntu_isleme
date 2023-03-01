"""
1 - Klavyeden girilen 5 tane sayıyı bir listeye atayarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
    ipucu : x = eval(input())
"""
liste = []
liste.append(eval(input("1. sayıyı giriniz :")))
liste.append(eval(input("2. sayıyı giriniz :")))
liste.append(eval(input("3. sayıyı giriniz :")))
liste.append(eval(input("4. sayıyı giriniz :")))
liste.append(eval(input("5. sayıyı giriniz :")))

def fonksiyon(n):
  return n*n - 20

liste.sort(key=fonksiyon)
print(liste)

'''
-5,   3, 10,   1,  7
 5, -11, 80, -19, 29
 1, 3, -5, 7, 10
'''
