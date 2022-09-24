#tek satrıda birden çok kullanımı

def hesapla(yas):
    yas += (yas * 0.20)
    return yas
def hesapla2(yas):
    yas += (yas * 0.05)
    return yas


yas = int(input("Yaşınızı Girin:  "))
biletsatis = hesapla(yas) if(yas >= 18 ) else hesapla2(yas) #
print(f" Yaşınız .: {yas}\nödeyeceginiz tutar :{biletsatis}₺")