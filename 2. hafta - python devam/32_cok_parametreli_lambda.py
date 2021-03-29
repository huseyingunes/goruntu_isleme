lambda_fonksiyonu = lambda a, b: a + b
print(lambda_fonksiyonu(5, 10))

lambda_fonksiyonu = lambda a, b, c: a + b + c
print(lambda_fonksiyonu(5, 10, 15))

def normal_fonksiyon():
    pass

print("Lambda nın Tipi:", type(lambda_fonksiyonu))
print("Normal Fonksiyonun Tipi:", type(normal_fonksiyon))


