import matplotlib.pyplot as plt
import numpy as np

# Données expérimentales
temperatures = [25, 30, 45.6]  # °C
pressions = [23.5, 26, 37.6]   # 10^5 Pa (Note : 37.6 est la Psat théorique du SF6 à Tc)

# Création de la figure
plt.figure(figsize=(10, 7))

# Tracé de la courbe de vaporisation
plt.plot(temperatures, pressions, 'ro-', linewidth=2, label='Courbe de vaporisation')


# Coloration des domaines
plt.fill_between(
    [25, 30, 45.6],           # x : Tes 3 températures
    [50, 50, 50],             # y1 : Le plafond (fixe à 50 pour les 3 points)
    [23.5, 26, 37.6],         # y2 : Ton nouveau plancher (tes 3 pressions de saturation)
    color='lightblue',
    alpha=0.3,
    label='Domaine Liquide'
)


plt.fill_between(temperatures, [23.5, 26, 37.6], 0,
                 color='orange', alpha=0.2, label='Domaine Vapeur')

# Délimitation zone supercritique
plt.axvline(x=45.6, color='gray', linestyle='--')

# Configuration des axes
plt.title('Diagramme de phase (P, T) du SF6', fontsize=14)
plt.xlabel('Température T (°C)', fontsize=12)
plt.ylabel('Pression P ($10^5$ Pa)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

# Ajustement des limites pour la clarté
plt.xlim(15, 60)
plt.ylim(0, 50)

plt.show()
