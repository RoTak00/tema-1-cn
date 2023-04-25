import numpy as np 
import math
import matplotlib.pyplot as plt

functie2 = lambda x : math.sin(x)
functie = lambda x : 1 / (1 + 25 * x * x)

def Verificare(A, b, tol = 10 ** -16):
    # Verificam ca A sa fie matrice bidimensionala
    if A.ndim != 2:
        print("Vectorul nu este bidimensional")
        return False

    # Verificam ca A sa fie matrice patratica
    if A.shape[0] != A.shape[1]:
        print("Matricea nu este patratica")
        return False    

    n = A.shape[0] # dimensiunea sistemului

    # Verificam ca b sa fie unidimensional 
    if b.ndim != 1:
        print("Vectorul b nu este unidimensional")
        return False
    # Verificam ca b sa aiba dimensiunea corecta
    if len(b) != n:
        print("Vectorul b nu are dimensiunea corecta")
        return False
    
    return True

def SubsAsc(A, b, tol = 10 ** -16):
    if Verificare(A, b, tol) == False:
        return None

    n = A.shape[0]

    # Verificam ca A sa fie inferior triunghiulara
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j]) > tol:
                print("Matricea nu e inferior triunghiulara")
                return None

    # Verificam ca sistemul sa fie compatibil determinat
    for i in range(n):
        if abs(A[i][i]) < tol:
                print("Sistemul nu e determinat")
                return None         

    # Calculam rezultatul sistemului
    res = np.zeros(n)
    for k in range(n):
        t = b[k]
        for j in range(k):
            t -= A[k][j] * res[j]

        t /= A[k][k]
        res[k] = t
    return res

def calcNewtonInX(x, C, vx):
    res = C[0]
    for i in range(1, len(C)):
        temp_prod = C[i]
        for j in range(i):
            temp_prod *= (x - vx[j])
        res += temp_prod

    return res



q = int(input("Puncte sau functie? 1 / 2\n"))
pts = []

if q == 1:
    x = int(input("How many points do you want to plot? "))
    pts = [[0, 0] for i in range(x)]
    for i in range(x):
        pt = [float(x) for x in input("Next point: ").split()]
        if len(pt) != 2:
            exit()
        pts[i] = pt
elif q == 2:
    a, b = [float(x) for x in input("Cele 2 capete\n").split()]
    n = int(input("Cate diviziuni?\n"))

    q2 = int(input("Tip diviziuni? (1 - normal / 2 - chebyshev)"))
    px = []

    if q2 == 1:
        px = np.linspace(a, b, n + 1)
    elif q2 == 2:
        px = np.array([(a + b) / 2 + ((b - a) / 2) * math.cos((n + i) * math.pi / n) for i in range(n + 1)])

    pts = [(x, functie(x)) for x in px]
else:
    print("Nu ai introdus corect.")
    exit(1)
    
pts = np.array(pts)
dim = len(pts)

px = np.array([x[0] for x in pts])
py = np.array([x[1] for x in pts])

A = np.zeros((dim, dim))

for i in range(dim):
    for j in range(0, i + 1):
        A[i][j] = 1

for j in range(1, dim):
    for i in range(j, dim):
        A[i][j] = A[i][j-1] * (px[i]-px[j-1])

C = SubsAsc(A, py)
print("C: \n")
print(C)

fig = plt.figure(1)
ax = plt.axes()

x = np.linspace(min([x[0] for x in pts]) - 0.01, max(x[0] for x in pts) + 0.01, 200)
y = calcNewtonInX(x, C, px)
if q == 2:
    y2 = np.vectorize(functie)(x)

ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'fun')
if q == 2:
    ax.plot(x, y2, linestyle="-", lw = 1, color = "g", label = "original")
ax.scatter([x[0] for x in pts], [y[1] for y in pts], color = 'r')

ax.grid(True, color = 'c')


ax.legend(loc='best')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Graph of the points / function requested')

ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')

plt.show()