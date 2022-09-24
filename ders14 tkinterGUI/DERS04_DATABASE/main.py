from  tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import database


pencere = Tk()
pencere.title("Veritabanı giriş")
pencere.geometry("900x600")

def dogrulama():
    try:
        if(len(txt_ogrNo.get()) == 0 or len(txt_ogrAdSoyad.get()) == 0 or len(txt_ogrBolumu.get()) == 0 or len(txt_ogrDTarihi.get()) == 0 or
          len(txt_ogrDYeri.get()) == 0 or len(txt_ogrSinifi.get()) == 0 or len(txt_ogrTuru.get()) == 0):
             msg.showerror(title="Dogrulama Hatası", message="Metin Kutuları boş geçilemez")
        else:
            if(len(txt_ogrAdSoyad.get()) <6 or len(txt_ogrAdSoyad.get())>20):
                msg.showinfo(title="Ad Soyad Bilgilendirme", message="ad ve Soyad Alanı 6 karakterden küçük olamaz\n Ad Soyad alanı 25 karakterden büyük olamaz")
            else:
                database.ekle()
                msg.showinfo(title="Veri tabanı kayıt", message="Bilgiler başarılı bir şekilde kaydedilmiştir.")
    except Exception as hata:
        msg.showerror(title="Bilinmeyen hata", message="Bilinmeyen Bir Hata Oluştu! Hata Kodu:\n{}".format(hata)) # msg boxta hatayı gösterir
        
        print(hata) #terminalde olşan hatatı gösterir


lbl_ogrNo = Label(pencere, text="Ögrenci No").place(x=100,y=100)
lbl_ogrAdSoyad = Label(pencere, text="Ad Soyad").place(x=100,y=130)
lbl_ogrDYeri = Label(pencere, text="Dogum Yeri").place(x=100,y=160)
lbl_ogrDTarihi = Label(pencere, text="Dogum Tarihi").place(x=100,y=190)
lbl_ogrTuru = Label(pencere, text="Ögreni Türü").place(x=100,y=220)
lbl_ogrBolumu = Label(pencere, text="Bölümü").place(x=100,y=250)
lbl_ogrSinifi = Label(pencere, text="Sınıfı").place(x=100,y=280)



txt_ogrNo = Entry(pencere, text="Ögrenci No")
txt_ogrNo.place(x=200,y=100)
txt_ogrAdSoyad = Entry(pencere, text="Ad Soyad")
txt_ogrAdSoyad.place(x=200,y=130)
txt_ogrDYeri = Entry(pencere, text="Dogum Yeri")
txt_ogrDYeri.place(x=200,y=160)
txt_ogrDTarihi = Entry(pencere, text="Dogum Tarihi")
txt_ogrDTarihi.place(x=200,y=190)
txt_ogrTuru = Entry(pencere, text="Ögreni Türü")
txt_ogrTuru.place(x=200,y=220)
txt_ogrBolumu = Entry(pencere, text="Bölümü")
txt_ogrBolumu.place(x=200,y=250)
txt_ogrSinifi = Entry(pencere, text="Sınıfı")
txt_ogrSinifi.place(x=200,y=280)

database.baglan()
btnEkle = Button(pencere, text="Ekle", width=12, command=dogrulama).place(x=120,y=320)
btnListele = Button(pencere, text="Listele", width=12, command=database.listele).place(x=220,y=320)
btnSil = Button(pencere, text="Sil", width=12,command=database.sil).place(x=120,y=350)
btnGüncelle = Button(pencere, text="Güncelle", width=12).place(x=220,y=350)

# --- treewiew kullanımı---

treeView = ttk.Treeview(pencere, column=("no"," column2"," column3", "column4",
                                         "column5","column6","column7"), show="headings", height=12)

# kolonları oluşturmak
treeView.column("#1",width=70, minwidth=50, anchor=CENTER ) 
treeView.column("#2",width=70, minwidth=50, anchor=CENTER ) 
treeView.column("#3",width=70, minwidth=50, anchor=CENTER ) 
treeView.column("#4",width=70, minwidth=50, anchor=CENTER ) 
treeView.column("#5",width=70, minwidth=50, anchor=CENTER ) 
treeView.column("#6",width=70, minwidth=50, anchor=CENTER ) 
treeView.column("#7",width=70, minwidth=50, anchor=CENTER ) 

#kolonları isimlendirmek
treeView.heading("#1", text="Ögrenci No" ) 
treeView.heading("#2", text="Ad Soyad" ) 
treeView.heading("#3", text="Dogum Yeri" ) 
treeView.heading("#4", text="Dogum Tarihi" ) 
treeView.heading("#5", text="Ögrenim Türü" ) 
treeView.heading("#6", text="Bölümü" ) 
treeView.heading("#7", text="Sınıfı" ) 

treeView.place(x=350,y=100)

def tabloGuncelle():
    for satir in treeView.get_children():
        treeView.delete()
    database.listele()

# sag tuş özelligi ekle

sagMenu = Menu(pencere, tearoff=0)
sagMenu.add_command(label ="Tabloyu Güncelle", command=tabloGuncelle)
sagMenu.add_command(label="Tabloyu Temizle"  )
sagMenu.add_command(label ="Sil",command=database.sil)
sagMenu.add_separator()
sagMenu.add_checkbutton()
sagMenu.add_radiobutton()
sagMenu.add_separator()



def sagTus(event):
    try:
        sagMenu.tk_popup(event.x_root, event.y_root)
        # treeview içinde herhangi tıklanan konumda açıl
    finally:
        sagMenu.grab_release()
        #ESC veya sol tuş tıklandıgında menüyü kapat
        

treeView.bind("<Button-3>", sagTus)


pencere.mainloop()