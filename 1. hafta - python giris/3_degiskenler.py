a =                             5
b=5.5
c = "metin"
d = True
e = 'e'
degisken = None

t:int = 5

from typing import Optional, Union

x: Union[str, None]
x: Optional[str]

print(a)
print(b)
print(c)
print(d)
print(e)

print("a nın değeri :", a,b,c,d,e, sep=" * ", end="|")
print("b nin değeri :", b)
print("c nin değeri :", c)
print("d nin değeri :", d)
print("e nin değeri :", e)
