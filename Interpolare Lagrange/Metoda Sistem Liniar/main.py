import numpy as np
import matplotlib.pyplot as plt

def reverse_poly(arr, x):
    res = 0
    for ind, val in enumerate(arr):
        res += (x ** ind) * val
    return res

def print_rev_poly(arr):
    for ind, val in enumerate(arr):
        if ind != 0:
            print(" + ", end="")
        print("%.3f" % val, end="")
        if ind != 0:
            print(f"x^{ind}", end="")
        print(" ", end="")

def Verificare(A, b):
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

x = int(input("How many points do you want to plot? "))
pts = [[0, 0] for i in range(x)]
for i in range(x):
    pt = [float(x) for x in input("Next point: ").split()]
    if len(pt) != 2:
        exit()
    pts[i] = pt


pts = np.array(pts)

fdim = len(pts)
print((fdim, fdim))
mat = np.zeros((fdim, fdim))
for ind, pt in enumerate(pts):
    for i in range(fdim):
        mat[ind][i] = pt[0] ** i

print(mat)
B = [x[1] for x in pts]
print(B)

sol = np.linalg.solve(mat, B)
print(sol)
print(reverse_poly(sol, 1))
print_rev_poly(sol)

ig = plt.figure(1)
ax = plt.axes()

x = np.linspace(min([x[0] for x in pts]) - 0.01, max(x[0] for x in pts) + 0.01, 200)
y = reverse_poly(sol, x)

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