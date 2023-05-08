import numpy as np

def citeste():
    dim = 0
    A = None
    B = None
    with open("in.txt", 'r') as file:
        dim = int(file.readline())
        A = np.zeros((dim, dim))
        for i in range(dim):
            A[i] = [float(x) for x in file.readline().split()]

        B = np.zeros(dim)
        B = [float(x) for x in file.readline().split()]

    return A, B

def GaussJordan(A, b, eps = 10 ** -16):
    A_extins = np.c_[A, b]
    n = A.shape[0]

    for k in range(n):
        p = k
        while p < n and abs(A_extins[p][k]) < eps:
            p += 1

        if abs(A_extins[p][k]) < eps:
            print("Sistemul nu este determinat")
            return None

        if k != p:
            A_extins[[k, p]] = A_extins[[p, k]]

        for l in range(n):
            if l != k :
                mlk = A_extins[l][k] / A_extins[k][k]
                A_extins[l] = A_extins[l] - A_extins[k] * mlk
    
    if abs(A_extins[n-1][n-1]) < eps:
        print("Sistemul nu este determinat")
        return None

    return A_extins

def Diagonala(diag):
    n = diag.shape[0]

    rez = np.zeros(n)
    for i in range(n):
        rez[i] = diag[i][n] / diag[i][i]
    return rez


A, B = citeste()

diag = GaussJordan(A, B)
print(diag)

res = Diagonala(diag)
print(res)