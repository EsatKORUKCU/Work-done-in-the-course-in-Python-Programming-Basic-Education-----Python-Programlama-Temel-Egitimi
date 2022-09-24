#Sözlük (dict) ve class yapısı kullanarak Kütüphane Otomasyonu Tasarımı

"""
1-Kitap Ekle
2-Yönetici Ekle
3-Kitap listele
4-Kitap Ara
5-Yönetici Listele
6-Çıkış

"""
from time import sleep
import os

class Yonetici:
    yoneticiSözlük = {}
    
    def yoneticiEkleme(self):
        self.yoneticiSicil = input("Yönetici Sicil No Girim   :")
        self.yoneticiAdi = input("Yönetici Adı soyadı Girim   :")
        self.yoneticiMaas = input("Yönetici Maası girim    :")
        
        self.yoneticiSözlük[self.yoneticiSicil] = {
            "yoneticiAdi" :self.yoneticiAdi,
            "toneticiMaas" :self.yoneticiMaas
        }
        sleep(1)
        print("Bilgiler Başarı ile eklendi")
        sleep(1)
        os.system("cls")
        
    def yoneticileriListele(self):
        if (self.yoneticiSözlük == {}):
            print("Yönetici Bilgisi Bulunamadı")
            sleep(1)
        else:
            for yonetici in self.yoneticiSözlük:
                print(yonetici, self.yoneticiSözlük[yonetici])
                sleep(2)
              
class BenimKutuphanem(Yonetici):
    kitaplarSozluk = dict()
    temizle = os.system("cls")
    def __init__(self):
        while True:
            os.system("cls")
            print("Kütüphane Otomasyonu".center(30,"*") )
            print("""
    1- Kitap Ekle
    2- Kitap listele
    3- Kitap Ara
    4- Yönetici Ekle
    5- Yönetici Listele
    6- Çıkış""")  
            secim = int(input("Seçiminizi (1-6)\t:  "))  
            if (secim ==1):
                self.kitapekle()
            elif secim ==2:
                self.kitapListele()
            elif secim == 3 :
                self.kitapAra()
            elif secim == 4:    
                super().yoneticiEkleme()
            elif secim == 5:
                super().yoneticileriListele() 
            elif secim == 6:
               self.cikis()
                  
            else:
                print("Hatalı Deger Girildi")  
                continue 
            
    def kitapekle(self):
        os.system("cls")
        tane = int(input("Kaç tane Kitap girilecek  : "))
        for adet in range(tane):
          self.kitapID = input("Kitap IG gir   :")
          self.kitapAdi = input("Kiatp Adı Gir   :")
          self.yazarAdi = input("Yazar Adı Gir   :")
          self.kitapTuru = input("Kitap Türü gir   :")
          self.kitapFiyat = float(input("Kitap fiyat gir   :"))
          self.kitaplarSozluk[self.kitapID] ={
              "kitapAdi": self.kitapAdi,
              "yazarAdi" : self.yazarAdi,
              "kitapTuru" : self.kitapTuru,
              "kitapFiyat" : self.kitapFiyat
          }
          sleep(0.5)
          print("Bilgiler kaydedildi  :")
          
    def kitapListele(self):
        os.system("cls")
        if len(self.kitaplarSozluk) == 0:
            print("Kayıtlı kitap bulunamadı")
            sleep(1)
        else:
            for kitap in self.kitaplarSozluk:
                print(kitap, self.kitaplarSozluk[kitap])
            sleep(2)
    
    def kitapAra(self):
        os.system("cls")
        self.kitapArama = input("Kitap ID sini Girin :  ")
        
        try:
            arama = self.kitaplarSozluk[str(self.kitapArama)]
            print(" Kitaplar Listeleniyor ".center(30,"═")) # alt + 205
            print("""
         Kitapm Adi .......:{}
         Yazar Adi.........:{}
         Kitap Türü .......:{}
         Kitap fiyat ......:{}""" .format(arama["kitapAdi"],arama["yazarAdi"], arama["kitapTuru"], arama ["kitapFiyat"]))
        except:
            print("Kitap bulunamadı")
            sleep(1)
    
    def cikis(self):
        print("Program Sonlandırılıyor...")
        exit(0)        
                 
    
    
            
kutuphane = BenimKutuphanem()