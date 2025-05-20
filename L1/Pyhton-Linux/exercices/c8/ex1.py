import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,1,100)
print(type(x))
y = x
y_1=x**2
y_2 = x**3
y_3 = x**4
plt.figure(1)
plt.plot(x,y, 'b', label="x")
plt.plot(x,y_1, 'r', label="x**2")
plt.plot(x,y_2, 'g', label="x**3")
plt.plot(x,y_3, 'm', label="x**4")
plt.xlabel('x')
plt.legend()
plt.show()
