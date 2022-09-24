#girilen 3 basamaklı sayının rakamları toplamı çift veya tek sayı oldugunu bulan prıgram

sayi = input("üç basamaklı sayı giriniz..")
toplam=0

if(len(sayi) != 3 or int(sayi[0]) == 0):
    print("Hatalı deger girildi")
    exit(0)
    
else:
    for rakam in range(3):
        toplam += int(sayi[rakam])
    if(toplam % 2 == 0):
        print("Rakamlar Toplamı Çiftttir.", toplam)    
    else:
        print("Rakamlar Toplamı Tektir.", toplam)