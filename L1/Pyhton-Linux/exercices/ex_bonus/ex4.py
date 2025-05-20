import numpy as np
import matplotlib.pyplot as plt
omega0=5
def application(n, omega, t):
    return (filtre((2*n+1)*omega0)*(4)/(np.pi*(2*n+1)*np.exp(1j*(2*n+1)*omega0*t)))

def y_app(t):
    y=0
    N=5
    for n in range(N):
        y = y + application(n, omega0,t)
        print(y,n)
    return y

def filtre(omega):
    return 1/(1+1j*(omega/omega0))

x = np.linspace(0,10,1000)
print(x)
y_resultat = []
for i in x:
    y_resultat.append(y_app(i))


print(y_resultat)
y_reel = np.real(y_resultat)
y_imag = np.imag(y_resultat)
print(y_reel)
fig, axs = plt.subplots(1,2)
#axs.reshape(-1)
axs[0].plot(x,y_reel, 'b', label="x")
axs[0].set_xlabel('Partie réelle')
axs[0].legend()

axs[1].plot(x,y_imag, 'b', label="x")
axs[1].set_xlabel('Partie imaginaire')
axs[1].legend()
plt.show()