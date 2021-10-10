import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return x**2+5

x1 = np.linspace(-1,1)
x2 = np.linspace(-6,6)
x3 = np.linspace(0,5)

plt.subplot(3,1,1)
plt.plot(x1,function(x1))


plt.subplot(3,1,2)
plt.plot(x2,function(x2))


plt.subplot(3,1,3)
plt.plot(x3,function(x3))

plt.show()
