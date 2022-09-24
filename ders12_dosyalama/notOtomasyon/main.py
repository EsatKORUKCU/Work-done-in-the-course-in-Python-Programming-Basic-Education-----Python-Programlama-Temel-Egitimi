# Öğrenci Not Otomasyonu Sistemi

def notGirisi():
    adSoyad = input("Öğrenci Adı Soyadı Girin.: ")
    odev = int(input("Odev Notu Girin.: "))
    vize = int(input("Vize Notu Girin.: "))
    final = int(input("Final Notu Girin.: "))
    
    with open("sinav.txt", "a", encoding="utf-8") as dosya:
        ogr = dosya.write(adSoyad + ":" + str(odev) + "," + str(vize) + "," + str(final) + "\n")
        print(ogr)
        
def notListele():
    pass

def harfNotuHesapla():
    pass

def main():
    while True:
        print("""Not Otomasyonu
    1- Öğrenci Not Girişi
    2- Öğrenci Not Listele
    3- Harf Notu Hesapla
    4- Çıkış""")
        secim = input("Seciminiz.: ")
        if secim == "1":
            notGirisi()
        elif secim == "2":
            notListele()
        elif secim == "3":
            harfNotuHesapla()
        else:
            print("hatalı deger")
main()
        