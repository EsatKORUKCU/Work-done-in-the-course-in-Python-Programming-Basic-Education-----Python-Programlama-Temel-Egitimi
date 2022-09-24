#kullanıacı adı ve sifre girildiginde  şifre dogruysa hoşgeldin mesajı versin
#şifre yanlış ise hatalı kullaıcı mesajı veren python programı

from pwinput import pwinput
from time import sleep

def kontrol(adısifre):
    bilgi = adısifre.split("-") # gelen listeyi - den ikiye böl ve bilagiye ata
    print() # bir satır terminalde boşlu bırakır
    while True:
        adi = input("kullanıcı adı gir:  ")
        sifre = pwinput("şifre gir: ", mask="*")
        
        if adi == bilgi[0]:
            if sifre == bilgi[1]:
                sleep(0.5)
                return print("Hoşgeldin",bilgi[0], "sistem açıldı..")
        else:
            return print("Kullanıcı adı veya şifre hatalı")
            continue
                
    


def main():
    #programın ana dosyaları burada çalışıyor ana fonksiyon her zaman en altta çalışır
    
    kullanici =[]
    with open("sifre.txt", "w", encoding="utf-8") as dosya:
        adı = input("Yeni Kullanıcı Adı Gir.:  ")
        sifre = pwinput("Yeni şfrenizi Gir.:", mask="*")
        kullanici.append(dosya.write(adı +"-"+ sifre))
        
    with open("sifre.txt", encoding="utf-8")  as dosya:
        for satır in dosya:
            kontrol(satır)
            
        


main()