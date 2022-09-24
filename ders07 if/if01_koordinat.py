#Koordinat düzlemi

xkoor = int(input("x Koordinat degeri girin.:"))
ykoor = int(input("ş Koordinat degeri girin.:"))

if (xkoor !=0 and ykoor !=0):   #! = Farklı demektir eşit degil
    if(xkoor>0):
        if(ykoor):
            print("1.Bölgededir")
        else:
            print("4.bölgededir.")
    else: # x in negatif olacagı kesin y yi bulacagız
        if(ykoor >0):
            print("2.bölgededir.")
        else:
            print(("3.Bölgedeir."))   
elif(xkoor ==0 and ykoor >0) or (xkoor ==0 and ykoor <0):
    print("y koordinatı üzerindedir.")
elif(ykoor==0 and xkoor>0) or (ykoor==0 and xkoor<0):  
    print("x koordinatı üzerindedir")        
else:
    print("Sayınız bölgede degildir\n başlangıçtadır")
    
    
    
    
    
    #pass #daha sonra yazılacak yere yazılır.