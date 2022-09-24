
topla = lambda s1,s2 : s1 + s2
fark = lambda s1,s2 :s1 - s2
ters = lambda ad : ad[::-1]


sayi1 = int(input("Birinci Sayı  :"))
sayi2 = int(input("İkinci sayı   :"))
metin = input("adınızı Yazın     :")

print("Sayılar Toplama     :", topla(sayi1,sayi2))
print("sayılar farkı       :",  fark(sayi1,sayi2))
print("Adınızın tersi      :", ters(metin))