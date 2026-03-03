a = 5
b = 5.5
c = "metin"
d = True
e = 'e'
f = None

from typing import Optional, Union

x: Union[str, None] = 5
y: Optional[str] = 5

print("a nın tipi :", type(a))
print("b nin tipi :", type(b))
print("c nin tipi :", type(c))
print("d nin tipi :", type(d))
print("e nin tipi :", type(e))
print("f nin tipi :", type(f))
print("x nin tipi :", type(x))
print("y nin tipi :", type(y))
