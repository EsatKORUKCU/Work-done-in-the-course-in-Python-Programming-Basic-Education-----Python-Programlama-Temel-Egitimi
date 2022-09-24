#Dışarıdan  girilen adede göre sözlüge kitap ekleyen program
import random, string

kutuphane= {}

harf = string.ascii_lowercase #alfabedeki kuçuk harfleri getirir.
adet= int(input("Kaç adet kitap girilecek.: "))

for sayi in range(1, adet+1):
    rdnSayi = str(random.randint(100, 999)) # 100 den 999  ararı rastgele sayı verir
    rdnHarf = random.choice(harf) # rastgele harf verir
    rdnKrktr = random.choice(string.punctuation) #özel karakterler
    kitapID = (rdnSayi+rdnHarf+rdnKrktr) # oluşturulan ID kitapID olatak atadı.
    KitapAdi = input("Kitap Adı Giriniz.: ")
    yazarAdi = input("Yazar Adı giriniz.: ")
    turu = input("Kitap Türü Giriniz.: ")
    fiyat = float(input("Kitap Fiyatı Giriniz.: "))
    
    kutuphane.update({
        kitapID:{
            "adi" :KitapAdi,
            "yazar":yazarAdi,
            "turu":turu,
            "fiyat":fiyat
        }
    })
    print()
    
#print() # bir satır boşluk ekle 
print(f"\n{kutuphane}") #print sola hizalı oldugunda for bittikten sonra kayıtları gösterir.

arananID =input("Aranılan Kitap ID si Girin.:")
if(kutuphane.get(arananID)==None):
    print("Aranan Kitap Bulunamadı")
else:
    kitap = kutuphane[KitapAdi]
    print("""
    Kitap Adı.: {}
    Yazar Adı.: {}
    Kitap Türü.: {}
    Fiyatı.:{}""".format(KitapAdi, yazarAdi, turu, fiyat))