listem = ["istanbul'u Dinliyorum","10", ".", "kaşagı", "fareler ve insanlar", "yaprak dökümü", "bilgisayara giriş"]
sayisalListe = [5,6,10,-1,-20,100,50]
sayisalListe.sort()
listem.sort()
 # Sayısal ifadelerde max min kulallanımı en büyük veya en küçük elemanları gösterir.Ayrıca metinsel listede lfabenin ilk karakterrine en yakın olan en küçük olur,son karaktere en uzak olan en büyük olur.
 # karışık listelerde bütütn elemanların aynı tip olması lazım (örnek:tümü metinsel) sayısal gerekli ise max ve min için bunları da çift tırnakta yazılmalı. sıralama ise önce özel karakter,sayısal ve harf olarak devam eder.
print("listenin En Büyük elemanı:\t", max(listem) )
print("listenin En Küçük elemanı:\t", min(listem) )

print("listenin En Büyük elemanı:\t", max(sayisalListe) )
print("listenin En Küçük elemanı:\t", min(sayisalListe) )

print ("Sayılar toplamı:", sum(sayisalListe)) #toplam degeri verir.
print(list(enumerate(listem, 1)))
print(list(enumerate(sayisalListe, 1)))# Verilen numarayı indis no vererek sıralı bir şekilde çıkyı alır.