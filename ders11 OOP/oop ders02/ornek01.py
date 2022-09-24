#python clas arası Miras(Kalıtım - Intheritance)


class Calisan:
    def __init__(self,adi,soyadi,maas):
        self.adi = adi
        self.soyadi = soyadi
        self.maas = maas
        self.eposta =(adi + "." + soyadi + "@sirket.com").lower()
        
    def bilgileriGoster(self):
        return """---Çalışan Bilgileri ---
        Adı........:{}
        Soyadı.....:{}
        Maası......:{}
        E-Posta....:{}""".format(self.adi,self.soyadi,self.maas,self.eposta) 
    
class Yazilimci(Calisan):
    def __init__(self, adi, soyadi, maas):
        super().__init__(adi, soyadi, maas)
        
    def programDili(self):
        self.progDili = input("Bildigi Program dili. :")
        return self.progDili
        
    def yazilimciListe(self):
         return """---Yazılımcı Bilgileri ---
        Adı............:{}
        Soyadı.........:{}
        Maası..........:{}
        E-Posta........:{}
        Program Dili...:{}""".format(self.adi,self.soyadi,self.maas,self.eposta, self.programDili()) 
        

class Yönetici(Calisan):
    pass



calisanAdi = input("Çalışan Adı Gir.: ")
calişanSoyadi = input("Çalışan Soyadı.: ")
calisanMaas = input("Çalışan Maas.:  ")

calisan1 = Calisan(calisanAdi,calişanSoyadi,calisanMaas)
yazilimci1 = Yazilimci(calisanAdi,calişanSoyadi, calisanMaas)

print(calisan1.bilgileriGoster())
print("Yazılımcı Bilgileri ".center(50, "-"))
print(yazilimci1.yazilimciListe())