# program içersinde oluşan hATAYI BELGEYE YAZDIRAN PYTHON PROGRAMI



try:
    sayi1 = int(input("Birinci Sayı gir:  "))
    sayi2 = int(input("İkinci Sayı Gir:   "))  
except Exception as hata:
    print("Hatalı Deger Girildi >", hata)
    with open("hata.txt", "w", encoding="utf-8") as dosya:
        print(hata, file=dosya)  
finally:
    print("Sayılar bölümü.:", sayi1/sayi2)