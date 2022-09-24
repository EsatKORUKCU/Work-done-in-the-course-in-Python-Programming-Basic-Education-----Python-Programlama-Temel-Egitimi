import sqlite3 # projeeye sqlite3 dahil edilir

with sqlite3.connect("veritabanı.db") as baglanti:

    imlec = baglanti.cursor() #veriler arasında gezinmek için cursır oluşturulur
    imlec.execute("create table if not exists ogrenci(kimlik INT,adi TEXT,soyadi TEXT,yas INT,sinifi TEXT, bolumu TEXT)") #tablo oluşturma sql sorgusu oluşturma yazdık

    imlec.execute("""insert into ogrenci values("bt22199","ahmt","Kara","40","Hazırlık","Bilgisayar Mühendisligi")""") #alanlara veriler ekleme işlemi
    baglanti.commit() #sql sorgusu işlenir.
