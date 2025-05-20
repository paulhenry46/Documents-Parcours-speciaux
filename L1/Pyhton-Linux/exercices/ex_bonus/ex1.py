import numpy as np
import matplotlib.pyplot as plt
def fact(n):
    nf=1
    for i in range(1,n+1,1):
        nf=nf*i
    return nf

x = range(1,8)
y=[]
for i in range(0,7):
    y.append(fact(x[i]))


plt.figure(1)
plt.plot(x,y, 'b', label="x")
plt.xlabel('x')
plt.yscale("log")
plt.legend()
plt.show()

# Créer un tableau de 3 vecteurs ligne
data = np.array([x, y])

# Transposer pour avoir une matrice à 3 colonnes (.T= transposition)
data = data.T
print(data)
# Définition du chemin du fichier
datafile_path = "./donnees4.txt"

# ecriture :
np.savetxt(datafile_path, data, fmt='%f', delimiter='\t')