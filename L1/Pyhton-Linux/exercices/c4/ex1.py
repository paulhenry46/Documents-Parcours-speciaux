import random as rand

n = int(input('nombre d\'éléménts'))
liste = []
for i in range(n):
    liste.append(rand.randint(0,20))

print(liste)

print('moyenne : ',sum(liste)/n)

