import numpy as np
import matplotlib.pyplot as plt

def f_k(x,k):
    return (x+1)*np.exp(k*x)
x= np.linspace(-3, 4, 100)

plt.plot(x, f_k(x,-3), '-b', label='k=-3')
plt.plot(x, f_k(x,-1), '-o', label='k=-1')
plt.plot(x, f_k(x,1), '-g', label='k=1')  # Graphique de y = x^2 de x=0 à x=3
plt.xlabel('Axe des X')
plt.ylabel('Axe des Y')
plt.title('Titre du graphique')
plt.legend()
plt.show()