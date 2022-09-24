import sqlite3

with sqlite3.connect("veritabanı.db") as baglantı:
    imlec = baglantı.cursor()
    imlec.execute("""update ogrenci set yas = 30 where kimlik="bt22105" """)