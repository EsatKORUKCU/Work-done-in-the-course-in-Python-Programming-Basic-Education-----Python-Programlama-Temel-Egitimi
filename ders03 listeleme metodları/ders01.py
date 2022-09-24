#listem = list()   liste oluşturmanın birirnci yöntemi
listem = ["İstanbul'u Dinliyorum", "kaşagı", "fareler ve insanlar"]
print(listem, "\t", type(listem))
print("Listemin uzunlugu :", len(listem))
print("iki aly çizgi ile uzunluk:", listem.__len__())

print(listem[0][::-1].upper()) # upper bütün kelimeleri büyük harf yapar.
sayi = int(input("0-2 arası sayı girin: ")) 
print(listem[sayi][::-1].upper())
