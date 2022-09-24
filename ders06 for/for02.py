#dışarıdan girilen adete göre girlen sayıya göre elEMn kaydeder ve yazar.
liste = []

adet = int(input("kaç eleman girilecek.:"))

for sayi in range(1, adet +1):
    eleman = input("{}. elemanı girin.: " .format(sayi))
    liste.append(eleman)

print(liste)
  
silmeAdet=int(input("kaç eleman silinecek.:   ")) 
if(len(liste) >= silmeAdet):

    listesilinen = [] # for ile silinen  elemanları buraya yazdır.

    for sayi in range(silmeAdet):
        elemansilinen =liste.pop() #her döndügünde sondan bir elemanı sil ve degişkene ata
        listesilinen.append(elemansilinen)
    print("\nsiilinen listesi.: ", listesilinen)
else:
    print("Silinen, listeden büyük olamaz")


    
    




"""
for eleman in liste:
     eleman2= input("Elaman Gir.:")
     liste.append(eleman2)
     """
    # bu döngü, listeye sonsuz elaman girmemizi saglar.