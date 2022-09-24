import tkinter as tk
from tkinter import messagebox

def mesaj():
    msg =  messagebox.showinfo( title="Bilgi kutusu", message="Giriş Dügmesine Tıklandı\nTebrikler")
   
def cikis():
    msg = messagebox.askquestion(title="Çıkış İşlemi", message="Çıkmak istiyormusunuz")
    if(msg == "yes"):
       # exit(0)
        pencere.destroy()

pencere = tk.Tk() # pencere nesnesini oluşturuyoruz
pencere.title("Tkinter dersine Hoşgeldiniz") #pencere başlıgı ekler
pencere.iconbitmap("mainicon.ico") # ikon eklmek için 
pencere.geometry("800x600+400+100") #pencere boyutunu ayarlama son iki deger ekranda her azamn nerede çıkacak yeri belirtir

pencere.maxsize(1000,800) # olabilecek en yüksek boyut
pencere.minsize(500,300) # olabilecek en küçük boyut
pencere.configure(bg="aqua") # sayfa arka plan zemin rengi
pencere.resizable(True,False) # pencere boyutu sabit mi degişken mi olsun

label = tk.Label(pencere, text="Burası İlk etiket bölümü", bg="red", font="Times 12 bold")
label.place(x=20,y=20) # penceredeki yerini x y yazılır paketleme yap
metin = tk.Entry(pencere, border = 2 ) # textbox kutusu
metin.place(x=200,y=20)

labeladi = tk.Label(pencere, text="Ad Soyad ", bg="maroon", fg="white",font="Times 12 bold")
labeladi.place(x=20,y=50) # penceredeki yerini x y yazılır paketleme yap
metin = tk.Entry(pencere, border = 2 )
metin.place(x=200,y=50)

labeladi = tk.Label(pencere, text="Parola ")
labeladi.place(x=20,y=80) # penceredeki yerini x y yazılır paketleme yap
metin = tk.Entry(pencere, cursor="Watch", show ="*" ) 
metin.place(x=200,y=80)

btnGiris = tk.Button(pencere, text="Giris", command=mesaj) # comman def fonk. çagırır
btnGiris.place(x=150,y=120, width =120, height=50  )

btnCıkıs = tk.Button(pencere, text="Çıkış", command=cikis)
btnCıkıs.place(x=300,y=120, width =120, height=50  )

canvas = tk.Canvas(pencere, bg="yellow")
canvas.place(x=400,y=50, width=100, height=100)

benimFontum = ("comic sans MS","20","italic bold")
labelfont = tk.Label(pencere, text = "Yazı karakteri Farklı", font = benimFontum, bg ="aqua" )
labelfont.place(x=120, y=200)

pencere.mainloop() # pencerenin ekranda sürekli açık kalmasını saglar