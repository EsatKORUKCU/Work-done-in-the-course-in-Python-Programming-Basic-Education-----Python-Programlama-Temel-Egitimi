def carpma(s1,s2):
    return lambda :s1 * s2

sayi1 = int(input("Birinci Carpan :"))
sayi2 = int(input("İkinci Carpan   :"))

carpim = carpma(sayi1, sayi2)
print(carpim())