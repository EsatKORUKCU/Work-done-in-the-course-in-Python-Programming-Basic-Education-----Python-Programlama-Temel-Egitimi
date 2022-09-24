#ögrenci not otomasyonu sistemi
from time import sleep as bekle
from os import system  as temizle

def notGirisi():
    temizle("cls")
    adSoyad = input("Ögrenci Adı Soyadı Girin:  ")
    odev = int(input("Ödev Notunu Girin: "))
    vize = int(input("Vize Notu Girirn:"))
    final = int(input("Final Notunu Girin:"))
    
    with open("sinav.txt","a", encoding="utf-8") as dosya:
        ogr = dosya.write(adSoyad + ":" + str(odev) + "," + str(vize) + "," + str(final) + "\n")
        print("ögrenci bilgileri kaydedilmiştir.")
    bekle(2)

def notListele():
    temizle("cls")
    print(" Ögrenci Notları" . center(25,"-"))
    with open("sinav.txt", encoding="utf-8") as dosya:
        for i in dosya:
            print(i, end="")
    bekle(2)

def notlarim(notlar):
    notlar = notlar[:-1]
    liste = notlar.split(":")
    ogrenciAdi = liste[0]
    ogrenciNotu = liste[1].split(",")
    
    odev = ogrenciNotu[0]
    vize = ogrenciNotu[1]
    final = ogrenciNotu[2]
    
    gecmeNotu = (float(odev)*0.1) + (float(vize)*0.4) +(float(final)*0.5)
    
    if(gecmeNotu >= 85 and gecmeNotu <=100):
        harfNotu = "AA"
    elif(gecmeNotu >= 70 and gecmeNotu <85):
        harfNotu = "BB"
    elif(gecmeNotu >= 60 and gecmeNotu <70):
        harfNotu = "CC"
    elif(gecmeNotu >= 50 and gecmeNotu <60):
        harfNotu = "DD"
    elif(gecmeNotu >= 0 and gecmeNotu <50):
        harfNotu = "FF"
    else:
        print("Gecersiz Not!")
    
    return ogrenciAdi + ":" + harfNotu + "\n"

def harfNotuHesapla():
    temizle("cls")
    with open("sinav.txt", encoding="utf-8") as dosya:
        harfliste = [] #harf notlarını ekleyecegimiz listeyi oluşturuluyor
        for satır in dosya:
            harfliste.append(notlarim(satır))

    with open("harfnotlarim.txt", "w", encoding="utf-8") as harfdosyasi:
        for satır in harfliste:
            harfdosyasi.write(satır)
    print("\nHarf Notları Başarı ile kaydedilmiştir.")
    bekle(2)

def harnotulistele():
    temizle("cls")
    print(" Ögrenci Notları" . center(30,"-"))
    with open("harfnotlarim.txt", encoding="utf-8") as dosya:
        for i in dosya:
            print(i, end="")
    bekle(2)
    
    
def main():
    while True:
        temizle("cls")
        print("""Not Otomasyonu
    1-Ögrenci Not Girişi
    2-Ögrenci Not Listele
    3-Harf Notu Hesapla
    4-Harf Notu Listele
    5-Çıkış""")
        secim = input("Seçiminiz.:")
        if secim == "1":
            notGirisi()
        elif secim == "2":
            notListele()
        elif secim == "3":
            harfNotuHesapla()
        elif secim == "4":
            harnotulistele()    
        elif secim == "5":
            bekle(1)
            print("sistem kapatılıyor")
            exit(0)
        else:
            print("hatalı deger")
            
            
main()