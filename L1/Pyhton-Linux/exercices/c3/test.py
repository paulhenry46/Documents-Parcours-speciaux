volume = 200
debit = 1.6
temps = 0
dt=1 #On peut choisir la précision que l'on souahite appliquer au programme. Plus dt est faible, plus il y aura d'itérations et plus le nombre d'heures écoulés sera précis. Cela n'a pas d'influence sur le résultat du nombre de jour puisqu'on l'affiche avec un chiffre après la virgule.

while volume > 0.1:
    temps = temps+dt
    volume = volume - (debit*dt)
    print('Il s\'est écoulé {:} heures et il reste : {:.2g} litres'.format(temps, volume))

jours = temps/24
print('Il faut {:.1f} jours pour vider le réservoir'.format(jours))
