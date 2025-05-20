import numpy as np
import matplotlib.pyplot as plt
def filtre(omega, omega_0, m):
    return (1)/(1+2*1j+m*(omega)/(omega_0)+(1j*omega/omega_0)**2)

def fonction_g(omega, omega_0, m):
    return 20*np.log(np.abs(filtre(omega,omega_0, m)))

omega=np.logspace(2,4,100)

valeurs = fonction_g(omega, 2000, 0.1)
print(valeurs)

fig, axs = plt.subplots(1,2)
#axs.reshape(-1)
axs[0].plot(omega,valeurs, 'b:', label="x")
valeurs_m = np.linspace(0,10,0.2)
print(valeurs_m)
for valeur in valeurs_m:
    y = fonction_g(omega, 2000, valeur)
    axs[0].plot(omega,y, 'b:', label="x")

axs[0].plot(omega,valeurs, 'b:', label="x")
axs[0].set_xlabel('Partie réelle')
axs[0].legend()


plt.show()