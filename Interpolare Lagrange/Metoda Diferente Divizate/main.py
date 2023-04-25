import numpy as np 
import matplotlib.pyplot as plt

# Calculate the value of the function in point x, based on the Lagrangian array arr
# and the point values from input
def fun(arr, pts, x):
    res = 0

    for i in range(len(arr)):
        subres = arr[i]
        for j in range(i):
            subres *= (x - pts[j][0])
        res += subres

    return res

# Print the form of the polynome based on the Lagrangian array arr
# and the point values from input
def printpoly(arr, pts):
    for i in range(len(arr)):
        if i != 0 and arr[i] > 0:
            print(" + ", end = "")
        elif i != 0 and arr[i] <= 0:
            print(" ", end = "")
        print("%.4f" % arr[i], end = "")
        for j in range(i):
            print(f"(x - ", "%.4f" % pts[j][0], ")", sep = "", end = "")

x = int(input("How many points do you want to plot? "))
pts = [[0, 0] for i in range(x)]
for i in range(x):
    pt = [float(x) for x in input("Next point: ").split()]
    if len(pt) != 2:
        exit()
    pts[i] = pt


pts = np.array(pts)

k = len(pts)

dd = np.zeros((k, k))

for i in range(k):
    dd[i, 0] = pts[i][1]

for j in range(1, k):
    for i in range(j, k):
        print(i, j)
        dd[i, j] = (dd[i, j - 1] - dd[i - 1, j - 1]) / (pts[i][0] - pts[i-j][0])

Q = np.zeros(k)
for i in range(k):
    Q[i] = dd[i,i]
print(Q)
printpoly(Q, pts)

fig = plt.figure(1)
ax = plt.axes()

x = np.linspace(min([x[0] for x in pts]) - 0.01, max(x[0] for x in pts) + 0.01, 200)
y = fun(Q, pts, x)

ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'fun')
ax.scatter([x[0] for x in pts], [y[1] for y in pts], color = 'r')

ax.grid(True, color = 'c')


ax.legend(loc='best')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Graph of the points requested')

ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')

plt.show()