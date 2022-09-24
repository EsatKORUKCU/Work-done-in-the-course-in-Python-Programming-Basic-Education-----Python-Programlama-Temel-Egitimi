kitaplık = {}

kitapID = int(input("Kitap ID Girin.:"))
adi = input("Kitap Adı Girin.:")
yazar = input("Yazar Adı Girin.:")
fiyat = float(input("fiyat Girin.:"))

kitaplık.update({
  "ID": kitapID,
  "adi": adi,  
  "yazar": yazar,
  "fiyat": fiyat
})

print()
print(kitaplık)