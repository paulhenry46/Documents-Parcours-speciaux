import numpy as np
np.linspace(0, 2*np.pi, 10) 
x= np.linspace(0, 2*np.pi, 10) 
y1= []
y2= []
for i in x:#Maniere pourrie
    y1.append(np.sin(i))
    y2.append(np.cos(i))
print(y1, y2)

# Créer un tableau de 3 vecteurs ligne
data = np.array([x, y1, y2])

# Transposer pour avoir une matrice à 3 colonnes (.T= transposition)
data = data.T
print(data)
# Définition du chemin du fichier
datafile_path = "./donnees3.txt"

# ecriture :
np.savetxt(datafile_path, data, fmt='%f', delimiter='\t')
x, y, z = np.loadtxt("./donnees3.txt", unpack=True)
print(x,y,z)