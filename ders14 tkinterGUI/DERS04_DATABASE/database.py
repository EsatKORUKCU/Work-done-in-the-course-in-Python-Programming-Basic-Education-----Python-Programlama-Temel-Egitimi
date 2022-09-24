import sqlite3,main
import tkinter as tk
import tkinter.messagebox as msg


def baglan():
    with sqlite3.connect("veritabani.db") as baglanti:
        imlec = baglanti.cursor()
        imlec.execute("create table if not exists ogrenci (no TEXT,adSoyad TEXT,dYeri TEXT,dTarihi TEXT,ogrTuru TEXT,bolumu TEXT,sinifi TEXT)")
        baglanti.commit()
        
def ekle():
    with sqlite3.connect("veritabani.db") as baglanti:
        imlec = baglanti.cursor()
        imlec.execute("""insert into ogrenci values("{}","{}","{}","{}","{}","{}","{}") """.format(
        main.txt_ogrNo.get(),
        main.txt_ogrAdSoyad.get(),
        main.txt_ogrDYeri.get(),
        main.txt_ogrDTarihi.get(),
        main.txt_ogrTuru.get(), 
        main.txt_ogrBolumu.get(),
        main.txt_ogrSinifi.get()
        ))
        baglanti.commit()
def listele():
    if(main.treeView.get_children()):
        msg.showwarning(title="Tablo Uyarısı", message="Tablo ")
    else:
        with sqlite3.connect("veritabani.db") as baglan:
            imlec = baglan.cursor()
            imlec.execute("select * from ogrenci")
            satirlar = imlec.fetchall() # bütün kayıtları getir
            
            for satir in satirlar:
                main.treeView.insert("", tk.END, values= satir)
            msg.showinfo(title="Listele", message="Kayıtlar Listelenmiştir.") 
def sil():
    try:
        with sqlite3.connect("veritabani.db") as baglan:
            imlec = baglan.cursor()
            secilensatir = main.treeView.selection()[0] # tıklandıgı ıd ait elemanı indis nosunu seçilen satıra atar
            
            for secilensatir in main.treeView.selection():
                imlec.execute(""" delete from ogrenci where no=? """,
                              (main.treeView.set(secilensatir, "no"),))
                baglan.commit()
        main.treeView.delete(secilensatir) # seçilen satırı siler
        msg.showinfo(title="Tablo Sil", message="Seçilen Kayıtlar Başarılı Bir şekilde silinmiştir.")
    except Exception as hata:
        msg.showerror(title="HATA", message="Bilinmeyen Bir Hata oluştu\n Hata Kodu.: {}".format(hata) )
        