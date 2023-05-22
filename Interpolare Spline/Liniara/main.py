import numpy as np
import matplotlib.pyplot as plt

def sortFun(el):
    return el[0]
def fun(px, n, x, a, b):
    for i in range(n):
        if x[i] <= px <= x[i+1]:
            return a[i] + b[i] * (px - x[i])
    return 0

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

slopes = []
for i in range(n - 1):
    slopes.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))

print(slopes)

plot_x = np.linspace(min(x), max(x), 200)
plot_y = []

current_ind = 0
for val in plot_x:
    if current_ind < n - 1 and val > x[current_ind + 1]:
        current_ind += 1
    plot_y.append(y[current_ind] + slopes[current_ind] * (val - x[current_ind]))

plot_y = np.array(plot_y)    

fig = plt.figure(1)
ax = plt.axes()


ax.plot(plot_x, plot_y, linestyle='-', lw = 2, color = 'b', label = 'fun')
ax.scatter([x[0] for x in pts], [y[1] for y in pts], color = 'r')

ax.grid(True, color = 'c')


ax.legend(loc='best')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Graph of the points requested')

ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')

plt.show()