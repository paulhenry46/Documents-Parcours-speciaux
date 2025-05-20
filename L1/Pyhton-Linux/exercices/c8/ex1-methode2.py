import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,100)
y = x
y_1=x**2
y_2 = x**3
y_3 = x**4

fig, axs = plt.subplots(2,2,figsize=(10,4))
# axs[0][0].plot(x,x**1, 'r')
# axs[0][0].set_xlabel('x')
# axs[0][0].set_ylabel('x**1')
# axs[0][0].legend(['x**1'])
# axs[0][0].set_ylim([0,1])

# axs[0][1].plot(x,x**2, 'r')
# axs[0][1].set_xlabel('x')
# axs[0][1].set_ylabel('x**2')
# axs[0][1].legend(['x**2'])
# axs[0][1].set_ylim([0,1])

# axs[1][0].plot(x,x**3, 'r')
# axs[1][0].set_xlabel('x')
# axs[1][0].set_ylabel('x**3')
# axs[1][0].legend(['x**3'])
# axs[1][0].set_ylim([0,1])

# axs[1][1].plot(x,x**4, 'r')
# axs[1][1].set_xlabel('x')
# axs[1][1].set_ylabel('x**4')
# axs[1][1].legend(['x**4'])
# axs[1][1].set_ylim([0,1])

i=1
for ax in axs.reshape(-1):
    
    ax.plot(x,x**i, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel(f"x**{i}")
    ax.legend([f"x**{i}"])
    ax.set_ylim([0,1])
    i=i+1

plt.show()
fig.savefig('graphique.png')