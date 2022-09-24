import sqlite3

with sqlite3.connect("veritabanı.db") as baglan:
    imlec = baglan.cursor()
    imlec.execute("""delete from ogrenci where kimlik ="bt22195" and soyadi="Kara" """)
    baglan.commit()