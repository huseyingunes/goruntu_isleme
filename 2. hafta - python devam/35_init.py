class Deneme:
    a = 10
    def __init__(self):
        print("Bu sınıftan bir nesne üretildi")
        print(self.a)


nesne = Deneme()
print(Deneme.a)
nesne.a = 15
print(Deneme.a)
print(nesne.a)

