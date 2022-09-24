# üç ve beşe tam bölünen yüzden küçük tam sayıların toplamı bulan python programı

def kontrol(sayi):
    if(sayi % 15 ==0):
        return True
    else:
        return False    


toplam = 0
sayiAdet = []
for i in range(1,100):
    if(kontrol(i)): # Buyazım if içi her zaman true döndürür.
        toplam += i
        sayiAdet.append(i)
        
print("Sayılar Toplamı: {}\n Sayı Adeti {}\n Sayılar {}" .format(toplam, len(sayiAdet), sayiAdet))        