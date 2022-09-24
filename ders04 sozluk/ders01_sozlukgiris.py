sozluk=  {
    "kitapID": 549,
    "adi": "Yaprak dökümü",
    "yazar": "Reşat Nuri Gültekin",
    "fiyat": 50.0
}

print(type(sozluk))
print(sozluk["kitapID"],sozluk["adi"])

#sözlükte olmayan degerlerin kontrolü
# print(sozluk["sayfasayisi"])
#sözlüklerde get metodu ile anahtar hata kontrolü yaptırılabilir.

print(sozluk.get("sayfasayisi", "anahtar yoktur."))
print(sozluk.values())
print(sozluk.items())