# n_1 = int(input('Nombre 1'))
# n_2 = int(input('Nombre 2'))

# liste_1 =[]
# liste_2 =[]

# for i in range(1,n_1+1):
#     print(i)
#     if n_1%i == 0:
#         liste_1.append(i)

# print(liste_1)

# for i in range(1,n_2+1):
#     print(i)
#     if n_2%i == 0:
#         liste_2.append(i)

# print(liste_2)

# liste = list(set(liste_1) & set(liste_2))
# print(max(liste))

##Généralisation
liste_diviseurs = []
nombres  = []

def liste_generateur(nombre: int, position):
    for i in range(1,nombre+1):
        #print(i)
        if nombre%i == 0:
            liste_diviseurs[position].append(i)

i = 1
message = 'Entrez le nombre : ', i, 'où tapez OK pour continuer'
while 1 == 1:
    entree = input(message)
    if(entree != 'OK'):
        nombres.append(int(entree))
        liste_diviseurs.append([])
        i=i+1
    else:
        break
i = 0
for nombre in nombres:
    liste_generateur(nombre, i)
    i = i+1

liste_1 = liste_diviseurs[0]
for sub_liste in liste_diviseurs:
   liste_1 =  set(liste_1).intersection(sub_liste)

print(max(liste_1))