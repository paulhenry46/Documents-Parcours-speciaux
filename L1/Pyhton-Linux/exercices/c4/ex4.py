n = int(input('nombre de nombres premier soyhaité'))



liste = [2]
i=1
nb_test=1
while i <n:
    premier = True
    for f in range(1,nb_test):
        if(nb_test % f ==0):
            premier = False
            
    if(premier == True):
        liste.append(nb_test)
        i=i+1
    
    nb_test=nb_test+1
    print(nb_test)
print(liste)

