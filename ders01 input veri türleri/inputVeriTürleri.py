sayi1=15
sayi2=30

toplam =sayi1+sayi2 # sayıları toplayıp değişkene atıyoruz


print("iki sayının toplamı.:",sayi1+sayi2)# normal yazım
print("formatlı iki sayı çarpım.: {}".format(sayi1*sayi2)) # formatlı yazım en sondadır
print(f"İki sayı farkı.: {sayi1-sayi2}") # f string kullanım en baştadır
print()
print("Sayıların Toplamı".center(50, "-"))
print("""    Birinci Sayı \t: {}
    İkinci Sayı \t: {}
    Sayılar Toplamı\t: {}""".format(sayi1,sayi2,toplam))