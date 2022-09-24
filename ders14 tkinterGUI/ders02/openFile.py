import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

pencere = Tk()
pencere.geometry("800x600")


def fotoekle():
    fotoDiolag = filedialog.askopenfilename(title="fotograf seçme", multiple=True, 
    filetypes=(("png", "*.png"),("jpg","*.jpg"),("bmp","*.bmp")) )
    
    for i in fotoDiolag:
        img = Image.open(i) # foto okunur ve açılır
        img = img.resize((300,300)) # new width height
        img = ImageTk.PhotoImage(img) # fotograf türünde oldugu belirtiliyor
        fotoEtiketi = Label(pencere) # Fotonun içine gonderilecegi etiket tanımlanıyor
        fotoEtiketi.place(x=100, y=100) # etiket konumlandırma
        fotoEtiketi.image = img # Fotograf etiketi eklenir
        fotoEtiketi["image"] = img
    
    
buton = Button(pencere, text="Fotograf Ekle", command=fotoekle)
buton.place(x=380, y=20)


pencere.mainloop()