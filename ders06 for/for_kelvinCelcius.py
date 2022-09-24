# kullanıcının alınan adete göre dereceyi(celcius) kelvin ve fahranayta çeviren program

dereceListe = []

adet = int(input("Kaç tane derece girecek.:"))
for derece in range(adet):
    d = int(input("derece girin.:  "))
    dereceListe.append(d)
    
kelvinListe = []
fahrebaytListe = list()

for santigrat in dereceListe:
    k = santigrat + 273 # kelvin degeri buluyoruz
    kelvinListe.append(k)
    f = santigrat * 1.8 + 32
    fahrebaytListe.append(f)

print(dereceListe, kelvinListe, fahrebaytListe, sep="\n")