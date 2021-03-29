class Deneme:
    a = 10
    def __init__(self):
        print("Bu sınıftan bir nesne üretildi")
        print(self.a)

    def adimi_yaz(self):
        print("Adım Deneme")

    def adimi_x_kere_yaz(self, a):
        print("Adım Deneme "*a)

    def __del__(self):
        print("Beni sildiler")

nesne = Deneme()
nesne.adimi_yaz()
nesne.adimi_x_kere_yaz(3)
print(dir(nesne))
del nesne
