sozluk = {
  "marka": "Ford",
  "model": "Mustang",
  "yil": 1964
}

print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])

sozluk["renk"] = "siyah"
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "beyaz"
print(sozluk)

print(sozluk.keys())
print(sozluk.values())

for i in sozluk.keys():
    print(i, ":", sozluk[i])
