#Agata Swatowska, zadanie 3- rysowanie wykresow funkcji x^2+5
import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return x**2+5

x1 = np.linspace(-1,1)
x2 = np.linspace(-6,6)
x3 = np.linspace(0,5)

fig, ax = plt.subplots(3,1)
fig.set_size_inches(6, 18)

y1 = function(x1)
ax[0].plot(x1, y1, label = 'x^2+5')
ax[0].set_ylabel("y")
ax[0].legend()
ax[0].set_title("wykres (-1, 1)")
ax[0].grid()

ax[1].plot(x2,function(x2), label = 'x^2+5')
ax[1].set_title("wykres (-6, 6)")
ax[1].set_ylabel("y")
ax[1].legend()
ax[1].grid()

ax[2].plot(x3,function(x3), label = 'x^2+5')
ax[2].set_title("wykres (0, 5)")
ax[2].set_ylabel("y")
ax[2].legend()
ax[2].grid()

plt.xlabel("x")
plt.show()
fig.savefig("wyk1.jpg")
