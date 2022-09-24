#iki deger arasındaki çift sayıları listeye yazdıran program
from winsound import Beep

buyuksayi = int(input("Başlangıç Sayısını Gir.: "))
kucuksayi = int(input("Bitiş sayısını Gir.: "))

ciftliste = []

if (buyuksayi > kucuksayi):
    for ciftMi in range(kucuksayi, buyuksayi):
        if(ciftMi % 2 ==0): # ciftmi ikiye tam bolunuyor mu
            ciftliste.append(ciftMi)
            
        else:
            continue
    print(ciftMi, ciftliste)    
    
elif(buyuksayi == kucuksayi):
    print("Sayılar eşittir", buyuksayi, kucuksayi)   
#else:
  #  Beep(2000, 1000)