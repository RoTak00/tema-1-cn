import numpy as np
import math
import matplotlib.pyplot as plt

fun = lambda x: math.log(x)

def reverse_poly(arr, x):
    res = 0
    for ind, val in enumerate(arr):
        res += (x ** ind) * val
    return res

def Directa(X, Y, x):
    mat = np.zeros((len(X), len(X)))

    for ind, pt in enumerate(X):
        for i in range(len(X)):
            mat[ind][i] = pt ** i
    
    sol = np.linalg.solve(mat, Y)

    return reverse_poly(sol, x)

def Newton(X, Y, x):
    A = np.zeros((len(X), len(X)))

    for i in range(len(X)):
        for j in range(0, i + 1):
            A[i][j] = 1

    for j in range(1, len(X)):
        for i in range(j, len(X)):
            A[i][j] = A[i][j-1] * (X[i]-X[j-1])

    C = np.linalg.solve(A, Y)

    res = C[0]
    for i in range(1, len(C)):
        temp_prod = C[i]
        for j in range(i):
            temp_prod *= (x - X[j])
        res += temp_prod

    return res

def DifDiv(X, Y, x):
    k = len(X)

    dd = np.zeros((k, k))

    for i in range(k):
        dd[i, 0] = Y[i]

    for j in range(1, k):
        for i in range(j, k):
            dd[i, j] = (dd[i, j - 1] - dd[i - 1, j - 1]) / (X[i] - X[i-j])

    Q = np.zeros(k)
    for i in range(k):
        Q[i] = dd[i,i]

    res = 0

    for i in range(len(Q)):
        subres = Q[i]
        for j in range(i):
            subres *= (x - X[j])
        res += subres

    return res

if __name__ == "__main__": 
    X = []
    Y = []
    with open("in.txt", "r") as file:
        X = [float(x) for x in file.readline().split()]
        Y = [fun(x) for x in X]
    

    print(X)
    print(Y)

    fig, ax = plt.subplots(2)

    x = np.linspace(min(X) - 0.01, max(X) + 0.01, 500)
    y1 = np.array([Directa(X, Y, elx) for elx in x])
    y0 = np.array([fun(elx) for elx in x])

    ax[0].plot(x, y1, linestyle='-', lw = 2, color = 'b', label = 'Interpolare Directa')
    ax[0].plot(x, y0, linestyle='--', lw = 2, color = 'g', label = 'Functie')
    ax[0].grid(True, color = 'c')

    ax[0].scatter(X, Y, color = 'r', label = "Puncte")

    ax[1].plot(x, np.vectorize(math.fabs)(y1 - y0), linestyle='-', lw = 2, color = 'b', label = 'Eroare Directa')
    ax[1].grid(True, color = 'c')
    ax[1].scatter(X, np.zeros(len(X)), color = 'r', label = "Puncte")

    plt.show()