class Bilisim:
    def __init__(self):
        self.ogretmen()
        self.dersAdi()
        self.dersMevcut()
        self.derslikNo()
    
    
    def ogretmen(self):
        ogretmen = input("Ögretmen giriniz : ")
        return print(ogretmen)
    
    
    def dersAdi(self):
        dersadi = input("Ders Adı giriniz : ")
        print(dersadi)
    
    
    def dersMevcut(self):
        dersmevcut = input("Mevcut giriniz : ")
        print(dersmevcut)
    
    
    def derslikNo(self):
        derslikno = input("Derslik No giriniz : ")
        print(derslikno)
   
class GenelMerkez:
    def __init__(self):
        super().__init__()
        
    def sinifYöneticisi(self):
        yoneticiAdi = input("Yönetici Adı gir : ")
        yöneticiMaas = int(input("Yönetici Maas gir : "))
        asistanAdi = input("Asistan Adı girin : ")
        print(dersler.dersAdi(), dersler.dersMevcut())
        print(yoneticiAdi, yöneticiMaas, asistanAdi)
   
dersler = Bilisim()
merkez = GenelMerkez()    

print(merkez.sinifYöneticisi())
    