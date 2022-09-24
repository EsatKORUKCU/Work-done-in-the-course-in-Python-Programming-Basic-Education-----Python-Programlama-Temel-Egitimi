import sqlite3 # projeeye sqlite3 dahil edilir

baglanti = sqlite3.connect("database.db") # veri tabanı baglantısı oluşturulur
imlec = baglanti.cursor() #veriler arasında gezinmek için cursır oluşturulur
imlec.execute("create table if not exists ogrenci(kimlik INT,adi TEXT,soyadi TEXT,yas INT,sinifi TEXT, bolumu TEXT)") #tablo oluşturma sql sorgusu oluşturma yazdık

imlec.execute("""insert into ogrenci values("bt22105","semih Can","Karakuş","20","Hazırlık","Bilgisayar Mühendisligi")""") #alanlara veriler ekleme işlemi
baglanti.commit() #sql sorgusu işlenir.
baglanti.close() # baglantıyı kapattık