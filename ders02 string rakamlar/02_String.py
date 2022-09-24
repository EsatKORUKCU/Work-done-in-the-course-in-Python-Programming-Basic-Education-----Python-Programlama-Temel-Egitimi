ad = input("Adını gir\t:")
soyad = input("Soyadını gir\t:")

birleştir = ad + soyad
print(birleştir[0]+ "\n"+birleştir[-1])
print("{} karakter sayısı: {}".format(birleştir, len(birleştir)))
# len() metodu karakter sayısını  bulmayı saglar

#indisler ile çalışma
print(birleştir[3:]) # 3.karakterden sonra yaz 
print(birleştir[:10]) # baştan 10.karaktare kadar yaz 

#atlayarak karakter sıralama
print(birleştir[2:12:3])
print(birleştir[::-1]) # karakter dizsini tersten sıralar
