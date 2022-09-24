from tkinter import *
from cgitb import text
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

pencere = tk.Tk()
pencere.title(" Tkinter İle İlk Projeme Hoş Geldiniz")
pencere.geometry("500x500")
pencere.resizable(False, False)
pencere.iconbitmap("icon.ico")
def mesaj():
    msg = messagebox.showinfo(title="Bilgi Kutusu", message="Giriş Düğmesine Tıklandı\nTebrikler")

def cikis():
    msg = messagebox.askquestion(title="Çıkış İşlemi", message="Çıkmak İstiyor Musunuz?")
    if(msg == "yes"):
        # exit(0)
        pencere.destroy()
def ekle():
    if(textVeri.get() == ""):
        window["text"] = "Geçersiz Değer"
    else:
         window["text"] = textVeri.get()

def sil():
    if(textVeri.get() != ""):
        textVeri.delete(0, "end")
    else:
        window["text"] = ""

resim = ImageTk.PhotoImage(Image.open("arkaplan.jpg"))
Label(pencere,  image=resim).place(x=0, y=0)

label = tk.Label(pencere, text="Kullanıcı Girişi", bg="black", fg="white", font=" Helvetica 17 italic " )
label.place(x=170, y=20)

labelAdi = tk.Label(pencere, text="Ad Soyad", bg="black", fg="white",font="Helvetica 10 italic  " )
labelAdi.place(x=110, y=60)
metinAdi = tk.Entry(pencere, border=2)
metinAdi.place(x=220, y=60)

labelAdi = tk.Label(pencere, text="Parola",bg="black", fg="white",font="Helvetica 10 italic  ")
labelAdi.place(x=110, y=90)
metinAdi = tk.Entry(pencere, cursor="Watch", show="*")
metinAdi.place(x=220, y=90)

buton = tk.Button(pencere, text="Giriş", width=10 ,bg="black", fg="white",font="10",command=mesaj)
buton.place(x=120, y=130)
buton = tk.Button(pencere, text="çıkış", width=10 ,bg="black", fg="white",font="13",command=cikis)
buton.place(x=240, y=130)

label = tk.Label(pencere, text="Taze Veri Girşi=>", bg="black", fg="white", font=" Helvetica 10 italic " )
label.place(x=110, y=180)
textVeri = tk.Entry(pencere, text="Veri Giriş", )
textVeri.place(x=225, y=180)


buton = tk.Button(pencere, text="Ekle", width=7 , bg="black", fg="white",font="10",command=ekle)
buton.place(x=110, y=210)
buton = tk.Button(pencere, text="Sil", width=7 ,bg="black", fg="white",font="13",command=sil)
buton.place(x=190, y=210)
buton = tk.Button(pencere, text="Güncelle", width=7 ,bg="black", fg="white",font="13")
buton.place(x=280, y=210)

labelAdi = tk.Label(pencere, text="TERMİNAL", bg="black", fg="white",font="Helvetica 12 italic  ")
labelAdi.place(x=180, y=260)
window = tk.Label(pencere, text="   ", width=28, height =5,bg="white", fg="black", font=" Helvetica 13 italic ")
window.place(x=90, y=300)


pencere.mainloop() 