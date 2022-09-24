from tkinter import *
import tkinter.messagebox as tm
#import psycopg2 as ps
import tkinter as tk
from PIL import Image, ImageTk



class log_in:
    def __init__(self,pencere):


        self.pencere=pencere
        self.pencere.geometry('250x100+500+200')
        self.pencere.title('Giriş')
        self.pencere.iconbitmap("icon.ico")
        self.resim = ImageTk.PhotoImage(Image.open("arkaplan2.jpg"))
        Label(self.pencere,  image=self.resim).place(x=0, y=0)
        self.Kullanıcı_Adi = Label(self.pencere,text='Kullanıcı Adı:', bg="black", fg="white",).grid(row=0,column=0)
        self.Paralo_Adi = Label(self.pencere, text='Parolanızı Giriniz:',bg="black", fg="white",).grid(row=1,column=0)
        self.Kullanıcı = Entry(self.pencere)
        self.Kullanıcı.grid(row=0,column=1)
        self.Parola = Entry(self.pencere,show="*")
        self.Parola.grid(row=1,column=1)

        self.Giris_Button = Button(self.pencere,text='   Giriş    ',bg="black", fg="white",width=7,command=self.giris_bolumu).place(relx=0.65,rely=0.45)

        self.Hatirla = Checkbutton(self.pencere,text='Beni Hatırla',bg="black", fg="white",).grid(row=3,sticky=W)


    def giris_bolumu(self,event = None):

        kullanıcı_bilgisi=self.Kullanıcı.get()
        paralo_bilgisi=self.Parola.get()

        if not self.Kullanıcı.get():
            bosluk=tm.askyesno(title="Hata!",
                               message="Gerekli yerleri doldurmadınız,tekrar giriş yapmak ister misiniz?")
            if bosluk == False:
                self.pencere.destroy()

        if (kullanıcı_bilgisi == 'esat') and (paralo_bilgisi == '1234'):
            self.olumlu=tm.showinfo('Giriş','Hoşgeldiniz')
            self.ekrani_temizle()


        if (kullanıcı_bilgisi != 'esat') and (paralo_bilgisi == '1234'):
            tm.showerror('Hata','Kullanıcı adınızı yanlış girdiniz')
        if (kullanıcı_bilgisi == 'esat') and (paralo_bilgisi != '1234'):
            tm.showerror('Hata', 'Parolanızı yanlış girdiniz')

    def ekrani_temizle(self):
        for widget in self.pencere.winfo_children(): # pencerede bulunan herşeyi kaldırdık
            widget.destroy()
        self.giris_tamam()

    def ekle(self):
         if(self.textVeri.get() == ""):
             self.window["text"] = "Geçersiz Değer"
         else:
              self.window["text"] = self.textVeri.get()

    def sil(self):
         if(self.textVeri.get() != ""):
            self.textVeri.delete(0, "end")
         else:
             self.window["text"] = ""


    def giris_tamam(self):
        self.resim = ImageTk.PhotoImage(Image.open("arkaplan.jpg"))
        Label(self.pencere,  image=self.resim).place(x=0, y=0)
        self.pencere.geometry("500x500+400+70")
        self.pencere.resizable(False, False)
        self.pencere.title('Veri güncelleme sayfası')
        
        
        self.label = tk.Label(pencere, text="Taze Veri Girşi=>", bg="black", fg="white", font=" Helvetica 10 italic " )
        self.label.place(x=110, y=180)
        self.textVeri = tk.Entry(pencere, text="Veri Giriş", )
        self.textVeri.place(x=225, y=180)

        self.buton = tk.Button(pencere, text="Ekle", width=7 , bg="black", fg="white",font="10", command=self.ekle)
        self.buton.place(x=110, y=210)
        self.buton = tk.Button(pencere, text="Sil", width=7 ,bg="black", fg="white",font="13",command=self.sil)
        self.buton.place(x=190, y=210)
        self.buton = tk.Button(pencere, text="Güncelle", width=7 ,bg="black", fg="white",font="13")
        self.buton.place(x=280, y=210)

        self.labelAdi = tk.Label(pencere, text="TERMİNAL", bg="black", fg="white",font="Helvetica 12 italic  ")
        self.labelAdi.place(x=180, y=260)
        self.window = tk.Label(pencere, text="   ", width=28, height =5,bg="white", fg="black", font=" Helvetica 13 italic ")
        self.window.place(x=90, y=300)
        
pencere=Tk()
uygulama=log_in(pencere)
pencere.mainloop()
