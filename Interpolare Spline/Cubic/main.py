import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as intrp
def sortFun(el):
    return el[0]

x = int(input("How many points do you want to plot? "))
pts = [[0, 0] for i in range(x)]
for i in range(x):
    pt = [float(x) for x in input("Next point: ").split()]
    if len(pt) != 2:
        print("Point wrong")
        exit()
    pts[i] = pt


pts = np.array(sorted(pts, key=sortFun))
x = [v[0] for v in pts]
y = [v[1] for v in pts]
n = len(pts)


plot_x = np.linspace(min(x), max(x), 200)
cs = intrp.CubicSpline(x, y)

fig = plt.figure(1)
ax = plt.axes()

ax.plot(plot_x, cs(plot_x), linestyle='-', lw = 2, color = 'b', label = 'fun')
ax.scatter([x[0] for x in pts], [y[1] for y in pts], color = 'r')

ax.grid(True, color = 'c')


ax.legend(loc='best')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Graph of the points requested')

ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')

plt.show()