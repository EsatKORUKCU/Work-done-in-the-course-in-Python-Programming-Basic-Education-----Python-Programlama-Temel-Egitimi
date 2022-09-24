# kullanıcıdan sürekli mesaj isteyen program programdan çıkış için q tuşuna basınız

mesaj = ""

while(True):
    soru = input("Bir mesaj giriniz (çıkış - q).:")
    if (soru == "q" or soru == "Q"):
        break
    else:
        pass