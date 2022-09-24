import sqlite3

with sqlite3.connect("veritabanı.db") as baglan:
    imlec = baglan.cursor()    
    imlec.execute("select * from ogrenci") #eleman filtreleme/listeleme
    for kayıt in imlec.fetchall(): # fetchall getir demektir
        print(kayıt) # terminale yazdır
    baglan.commit()