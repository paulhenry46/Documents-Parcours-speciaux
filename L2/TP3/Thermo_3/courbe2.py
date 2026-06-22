import matplotlib.pyplot as plt
import numpy as np

# Données rectifiées pour le Fréon (P en 10^5 Pa, T en °C)
# Ajout du point critique (T=100, P=40)
temperatures_freon = [20, 30, 40, 50, 100]
pressions_freon = [6, 8, 10, 15, 40]

# Création de la figure
plt.figure(figsize=(10, 7))

# Tracé de la courbe de vaporisation du Fréon
plt.plot(temperatures_freon, pressions_freon, 'bo-', linewidth=2, label='Courbe de vaporisation (Fréon)')

# Coloration du domaine Liquide (au-dessus de la courbe)
# Plafond à 60 pour englober le point critique et laisser de la place
plt.fill_between(
    temperatures_freon,
    60,
    pressions_freon,
    color='lightblue',
    alpha=0.3,
    label='Domaine Liquide'
)

# Coloration du domaine Vapeur (en-dessous de la courbe)
plt.fill_between(
    temperatures_freon,
    pressions_freon,
    0,
    color='orange',
    alpha=0.2,
    label='Domaine Vapeur'
)

# Délimitation zone supercritique (verticale au point critique)
plt.axvline(x=100, color='gray', linestyle='--')

# Configuration des axes
plt.title('Diagramme de phase (P, T) du Fréon', fontsize=14)
plt.xlabel('Température T (°C)', fontsize=12)
plt.ylabel('Pression P ($10^5$ Pa)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

# Ajustement des limites pour voir l'ensemble jusqu'au point critique
plt.xlim(10, 120)
plt.ylim(0, 60)

plt.show()
