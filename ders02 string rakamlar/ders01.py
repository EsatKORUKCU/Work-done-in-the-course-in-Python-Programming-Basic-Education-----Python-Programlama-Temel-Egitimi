taban=int(input("Taban sayısı gir"))
us=int(input("Us sayısını gir"))

usAlma = taban ** us
print("sayılar karesi.: {}" .format(usAlma))
print("Burasıda pow ile yazıldı",pow(taban, us))
print("Mod Alma.:".center(20,"*"))
mod = taban % us
print("{} - Tabanın  {} - Use bölümünden kalan:{}" .format(taban, us, mod))
print()
bolum=taban/us          # / normal bölme yapar
tamBolme = taban // us  # // tam bölme yapar
print("Sayıların tam bölümü.: {}\nSayıların Normal Bölümü.:{}" .format(tamBolme,bolum))


