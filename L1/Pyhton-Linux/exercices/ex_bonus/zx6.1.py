import numpy as np
import matplotlib.pyplot as plt

li = [1, 2, 3] # une liste
a = np.array(li) # un array :-)

# Intervalles et espacements
b = np.arange(0, 10, 2)  # Commence à 0, finit avant 10, pas de 2
c = np.linspace(0, 10, 5)  # Commence à 0, finit à 10, 5 éléments
d = np.logspace(0, 3, 4)  # Espace logarithmique: commence à 10^0, finit à 10^3, 4 éléments

x = np.arange(4)
y = x**2
z = x**3
# Création de graphique
plt.plot(x, y, '-o', label='x**2')  # Graphique de y = x^2 de x=0 à x=3
plt.plot(x, z, '-xr', label='x**3')  # Graphique de z = x^3 de x=0 à x=3
plt.xlabel('Axe des X')
plt.ylabel('Axe des Y')
plt.title('Titre du graphique')
plt.legend()
plt.grid(True)
plt.show()