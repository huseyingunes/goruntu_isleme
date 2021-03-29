class Deneme:
    a = 10
    def __init__(self):
        #print("Bu sınıftan bir nesne üretildi")
        #print(self.a)
        pass

    def adimi_yaz(self):
        print("Adım Deneme")

    def adimi_x_kere_yaz(self, a):
        print("Adım Deneme "*a)

    def __del__(self):
        #print("Beni sildiler")
        pass

    def __str__(self):
        return "a nın değeri : "+str(self.a)


nesne = Deneme()
print(nesne)
