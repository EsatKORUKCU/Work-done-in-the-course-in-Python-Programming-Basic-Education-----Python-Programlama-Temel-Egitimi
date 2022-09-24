class BilisimOkulu:
    derslikNo = 303
    dersAdi = "Python Programlama"
    ogretmen = "Sercan Tırmık"
    mevcut = 10
    
    
class GrafikTasarim:   
    derslikNo = 202
    dersAdi = "Photoshop"
    ogretmen = "Keremcem Cem"
    mevcut = 20
    
    def ogretmenDegistir(self):
        self.ogretmen = input("Ogretmen Adı Giriniz.: ")
        return self.ogretmen



derslik1 = BilisimOkulu()
derslik2 = GrafikTasarim()

print(type(derslik1))
print("Derslik No: {} \n Ders Adı: {}\nOgretmen: {}\nMevcut {}" .format(derslik1.derslikNo, derslik1.dersAdi, derslik1.ogretmen, derslik1.mevcut))
print()
print("Derslik No: {} \n Ders Adı: {}\nOgretmen: {}\nMevcut {}" .format(derslik2.derslikNo, derslik2.dersAdi, derslik2.ogretmenDegistir(), derslik2.mevcut))