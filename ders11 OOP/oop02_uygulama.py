toplalist = []
carplist = []

class ToplaCarp:
    def __init__(self,sayı1, sayı2):
        self.s1 = s1
        self.s2 = s2
    
    def topla(self):
        toplami = self.s1 + self.s2
        print("Sayılar toplamı   :", toplami)
        toplalist.append(toplami)
        
        
    def carpim(self):
        carpimi = self.s1 * self.s2
        print("Sayılar çarpımı  :", carpimi)
        carplist.append(carpimi)
    
    
while True:
    try:
        s1 = int(input("Birinci Sayı Gir : "))
        s2 = int(input("ikinci sayı gir : "))
        sayi = ToplaCarp(s1,s2)
        sayi.topla()
        sayi.carpim()
        durum = input("\nYeni Deger Girilsin Mi (e-h):").lower()
        if(durum == "e" ):
            continue
        elif(durum =="h"):  
            exit(0)
        else:
            print("Are You Kidding Me :v")
            break
    except Exception as hata:
        print("Yanlış deger girildi")