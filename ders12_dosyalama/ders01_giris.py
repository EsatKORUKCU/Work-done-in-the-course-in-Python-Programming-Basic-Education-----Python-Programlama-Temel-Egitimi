# Okuma modu ile çalışma ve hata kontrolü

dosya = open("deneme.txt",  encoding ="utf-8") # Dosya r modu ile okunursa modu yazmaya gerek yoktur.
okuma = dosya.read()
print(okuma)
dosya.close()

try:
    # Daha önce oluşturulmayan dosyayı okuma ile açmaya çalışıyor
    #verilen hatayı terminalde gösterme.
    with open("denemehata.txt") as file:
        icerik = dosya.read()
    
except Exception as hata:
    print("Hata Var>", hata)
        