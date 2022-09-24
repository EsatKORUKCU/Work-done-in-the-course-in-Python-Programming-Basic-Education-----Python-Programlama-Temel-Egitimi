# küpün alan hacim çevresini hesaplayan program
from time import sleep # bekletme saglar sleep içersinde saniye sleep(1)
import os # konsolda bulunan sistem komutlarını çalıştırır.

def alan(s):
    return 6*s**2

def hacim(s):
    return s**3

def cevre(s):
    return 12*k

def main():
    kenar = int(input("Kenatr Uzunlugu Giriniz: "))
    while True:
        print("küp - Alan, Hacim, Çevre" .center (50,"-"))
        print("""
        1.Alan
        2.Hacim
        3.Çevre
        4.Çıkış""")
        secim = int(input("Seçiminizi Yapın:  "))
        if(secim < 1 or secim > 4):
            print("Hatalı Seçim")
            os.system("cls")
        elif(secim == 1):
            print(alan(kenar)) 
            sleep(1)  # bekleme yapar
            os.system("cls")
        elif(secim == 2):
            print(hacim(kenar))
            sleep(1)
            os.system("cls")
        elif(secim == 3):
            print(cevre(kenar))
            sleep(1)  
            os.system("cls")
        elif(secim ==4 ):
            exit(0)
        else:
            print("Sadcece tam sayı giriniz")
main()