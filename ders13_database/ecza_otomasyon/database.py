import sqlite3,main



def baglanti(): # tablo ve database oluşturulur
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" create table if not exists eczane(
            adi TEXT , 
            firma TEXT, 
            turu TEXT,
            fiyat FLOAT,
            stoktaMi BOOL
            ) """)
        baglan.commit()

def ekle():
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" insert into eczane values ("{}","{}","{}","{}","{}")  """.
        format(
           main.kutuphane1.ad,
           main.kutuphane1.uretici,
           main.kutuphane1.turu,
           main.kutuphane1.fiyat,
           main.kutuphane1.stoktaMi
        ))
        baglan.commit()
        
def listele():
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" select * from eczane """)
        ilaclar = imlec.fetchall()
        metineCevir = lambda * arguman : [str (y) for y in arguman]
        for sayi, eleman in enumerate(ilaclar, 1):
            print("{}- {}".format(sayi, "".join(metineCevir(eleman))))
        baglan.commit()
        
def sil():
    listele()
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        while True:
            try:
                secim = int(input("Silinicek ilac No Girin. ."))
                break
            except Exception:
                print("Geçersiz Deger Girdiniz.")
                
    imlec.execute(f"""delete from eczane where rowid={secim}""")
    baglan.commit()
    
def guncelle():
    
    listele()
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        while True:
            try:
                secim = int(input("Güncellenecek ilac No Girin. ."))
                break
            except Exception:
                print("Geçersiz Deger Girdiniz.")
        
        while True:
            try:
                guncellesecim = int(input(""" Güncellenek alan adını seçin
    1-ADI
    2-URETİCİ FİRMA
    3-TURU
    4-FİYAT
    5-STOK DURUMU
    
seçiminiz.........:"""))
                if guncellesecim <1 or guncellesecim >5:
                 break
            except Exception:
                print("Sayısal bir deger giriniz")
            alanAdları = ["adi ","firma","turu ","fiyat","stoktaMi"]
            yeniDeger = input("Yeni Deger Girin ...:")
            
            imlec.execute(""" update eczane set {} = "{}" where rowid={} """.format
            (alanAdları[guncellesecim-1], yeniDeger,secim))
            baglan.commit()
            break
          