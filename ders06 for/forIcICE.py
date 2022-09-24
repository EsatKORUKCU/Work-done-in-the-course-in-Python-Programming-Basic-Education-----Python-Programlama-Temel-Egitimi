#çarpım tablosu uygulaması

for i in range(1 ,11):
   # print("\t")
    print(" ".center(15," "))
    for j in range(1, 11):
        print("{}x{}={}".format(i, j, i*j),end="\t")