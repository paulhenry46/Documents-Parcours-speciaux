import numpy as np
import matplotlib.pyplot as plt

# Paramètres
omega_t = np.linspace(0, 4 * np.pi, 1000)  # Deux périodes
phi_max = 1.0  # Valeur arbitraire pour l'amplitude du flux
i_max = 0.8    # Valeur arbitraire pour l'amplitude de l'intensité (e.g. Bm * omega * S / R)

# Fonctions
# phi(t) = Phi_max * cos(omega * t)
phi = phi_max * np.cos(omega_t)

# e(t) = -dphi/dt = Phi_max * omega * sin(omega * t)
# i(t) = e(t) / R -> proportionnel à sin(omega * t)
courant = i_max * np.sin(omega_t)

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(omega_t, phi, label=r'Flux $\phi(\omega t)$', color='blue', linewidth=2)
plt.plot(omega_t, courant, label=r'Courant $i(\omega t)$', color='red', linestyle='--', linewidth=2)

# Configuration des axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Graduations en multiples de pi/2
ticks = np.arange(0, 4.5 * np.pi, np.pi / 2)
labels = [r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$', 
          r'$5\pi/2$', r'$3\pi$', r'$7\pi/2$', r'$4\pi$']
plt.xticks(ticks, labels)

# Esthétique
plt.title(r'Loi de Lenz : Relation entre $\phi$ et $i$', fontsize=14)
plt.xlabel(r'$\omega t$ (rad)')
plt.ylabel('Amplitude (Unités arb.)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("induction_lenz.pdf")
plt.show()