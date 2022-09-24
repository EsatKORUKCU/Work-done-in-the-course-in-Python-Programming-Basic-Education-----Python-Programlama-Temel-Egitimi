







listem = ["İstanbul'u Dinliyorum", "kaşagı", "fareler ve insanlar"]

kitap = input("Kitap adı Girin:")
listem.insert(1, kitap) # verilen indis numarasına göre eleman ekler.
kitap2 = input("Diger kitap  adı girin:")
listem.append(kitap2) #Girileni en sona ekler.
kitap3 = input("Son kitabı gir artık.:")
listem.extend(kitap3) # Girilen elemanın her karakterini ayrı eleman olarak tutar.
olmayankitap= input("Kitap Adı Girin.:")
print(kitap2, "Liste içindemi.:", kitap2 in listem)
print(listem)