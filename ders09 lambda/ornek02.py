# 2 üzeri deger girildiginde üssü degerrinde basamakları toplamındaki sayı kaçtır.
def basamaktoplamı(a):
    uslusayi = 2**a 
    toplam = 0
    for basamak in str(uslusayi):
        toplam += int(basamak)
    return toplam

def sayi(a):
    return 2**a




usDegeri = int(input("2 üzeri kaç olsun: "))
toplam = basamaktoplamı(usDegeri)
print("{} Sayısının Basamak degerleri toplamı.: {}" .format(sayi(usDegeri), toplam))