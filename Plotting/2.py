import numpy as np
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(3, 1)

x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)

x2 = np.linspace(0, 5, 100)
y2 = np.cos(3 * x2)

t = np.linspace(0, 2 * np.pi, 100)
x3 = 2 * np.cos(t)
y3 = 2 * np.sin(t)

ax[0].plot(x1, y1, linestyle = "-", lw = 2, color = 'b', label = 'y = sin(x)')
ax[0].legend(loc='best')
ax[0].set_xlim([0, 10])
ax[0].set_ylim([-1.2,1.2])
ax[0].axis('equal')
ax[0].grid()

ax[1].plot(x2, y2, linestyle = "-", lw = 2, color = 'y', label = 'y = cos(3x)')
ax[1].legend(loc='best')
ax[1].set_xlim([0, 10])
ax[1].set_ylim([-1.2,1.2])
ax[1].grid()

ax[2].plot(x3, y3, linestyle = "-", lw = 2, color = 'r', label = 'r = 2 circle')
ax[2].legend(loc='best')
ax[2].set_xlim([-3, 3])
ax[2].set_ylim([-3.2,3.2])
ax[2].axis('equal')
ax[2].grid()

plt.show()
