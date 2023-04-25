import numpy as np
import matplotlib.pyplot as plt 

fig = plt.figure(1)
ax = plt.axes()

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = sin(x)')
ax.grid(True, color = 'c')

plt.xticks(np.arange(-4,4,1))
plt.yticks(np.arange(-1.5,1.6,0.5))

ax.legend(loc='best')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Graph of y = sin(x) on int [-pi, pi]')

ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')

plt.show()
