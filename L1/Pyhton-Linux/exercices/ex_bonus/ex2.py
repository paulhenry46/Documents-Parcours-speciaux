import numpy as np
import matplotlib.pyplot as plt

sup = 2
inf = 1
m = (sup+inf)/2
sqrt2 = 2**0.5
precision = int(input('precision'))
n=0
table= []
while sup-inf > 10**(-precision-1):
    m = (sup+inf)/2
    if(m > sqrt2):
        sup = m
    else:
        inf=m
    n=n+1
    table.append(m)
    
    #table.append(m)
m = round((sup+inf)/2, precision)
print(m, sup, inf)
print(len(table))
print(n)

#plt.figure(1)
#plt.plot(range(n),table, 'b', label="x")
#plt.xlabel('x')
#plt.legend()
#plt.axhline(2**0.5,color='r', linestyle="--")
#plt.show()

number_values=6
last_values=[]
for i in range(number_values):
    last_values.append(table[-(i+1)])
print(table,last_values )

fig, axs = plt.subplots(1,2)
#axs.reshape(-1)
axs[0].plot(range(n),table, 'b', label="x")
axs[0].set_xlabel('x')
axs[0].legend()
axs[0].axhline(2**0.5,color='r', linestyle="--")

axs[1].plot(range(n-6, n),last_values, 'b', label="x")
axs[1].set_xlabel('x')
axs[1].legend()
axs[1].axhline(2**0.5,color='r', linestyle="--")
plt.show()