import numpy.random as rd
import matplotlib as plt
liste = rd.randint(1, 5, 1000)

value_0_2 = 0
value_2_4 = 0
value_4_6 = 0
value_6_8 = 0
value_8_10 = 0

for i in liste:
    if 0<=i<2:
        value_0_2 = value_0_2 + 1
    elif 2<=i<4:
        value_2_4 = value_2_4 + 1
    elif 4<=i<6:
        value_4_6 = value_4_6 + 1
    elif 6<=i<8:
        value_6_8 = value_6_8 + 1
    elif 6<=i<8:
        value_6_8 = value_6_8 + 1
    elif 8<=i<10:
        value_8_10 = value_8_10 + 1

plt.bar()