with open("yazma.docx","a",encoding="utf-8") as dosya:
    bilgi = input("Belge içine ne yazılsın: ")
    icerik = dosya.writelines(bilgi)
    print(icerik)