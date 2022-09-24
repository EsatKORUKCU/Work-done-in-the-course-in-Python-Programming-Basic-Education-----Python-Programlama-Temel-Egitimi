

yıl = int(input("yıl giriniz.."))

if((yıl % 400 ==0) or (yıl % 4 == 0 and yıl % 100 != 0)):
    print("artık yıl.:", yıl)
else:
    print("artık yıl degil.:",yıl)