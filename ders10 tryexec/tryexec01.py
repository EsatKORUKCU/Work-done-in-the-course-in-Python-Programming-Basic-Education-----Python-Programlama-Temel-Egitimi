

try:
    s1 = int(input("s1 gir"))
    s2 = int(input("s2 gir"))
    bolme = s1/s2
except Exception as hata:
    print(hata)
else:
    print("işlem Hatasız Çalışıyor\nSonuc : ", bolme)
finally:
    print("Finally her durumda çalışır.")
