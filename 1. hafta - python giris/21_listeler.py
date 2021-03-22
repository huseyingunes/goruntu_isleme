liste = ["Elma", "Armut", "Ayva"]
print(liste)

print(liste[1])

print(len(liste))

list2 = [1, 5, 7, 9, 3]
list3 = [True, 2, "ASDF"]

print(list3)

print(liste[1:3])

if "Elma" in liste:
    print("Listede elma da varmış..")

liste[1] = "Kiraz"
print(liste)
liste.append("Çilek") # listenin sonuna Çilek elemanını ekler
print(liste)
liste.insert(0, "Ananas") # listenin başına Ananas elemanını ekler
print(liste)

liste.remove("Ananas") # listedeki değeri Ananas olan elemanı siler
print(liste)
liste.pop(1) # listenin 1. elemanını siler
print(liste)
liste.pop() # listenin sonundan bir eleman siler
print(liste)
del liste[0] # listenin ilk elemanını siler
print(liste)
liste.clear() # listeyi temizler
print(liste)


