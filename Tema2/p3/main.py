import numpy as np

def readLinearSystem(path):
    dim = 0
    mat = ""
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [float(x) for x in file.readline().split()]

    return mat[:, :dim], mat[:, dim:].T[0]

def citireDate(path):
    A = np.array([])
    b = np.array([])

    c = 0
    d = 0
    f = 0
    n = 0
    with open(path, 'r') as file:
        c = float(file.readline())
        d = float(file.readline())
        f = float(file.readline())
        n = int(file.readline())

    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(n):
        A[i,i] = d
        if i == 0:
            continue
        A[i, i-1] = c
        A[i - 1, i] = f

    b[0] = 2
    b[n-1] = 2
    for i in range(1, n-1):
        b[i] = 1

    return A, b


def FactorizeLR(A):
    dim = A.shape[0]

    L = np.identity(dim)
    R = np.zeros((dim, dim))

    R[0,0] = A[0,0]
    for i in range(dim-1):
        L[i+1,i] = A[i+1,i] / R[i,i]
        R[i,i+1] = A[i, i+1]
        R[i+1,i+1] = A[i+1, i+1] - L[i+1,i] * R[i,i+1]

    return L, R

def SolveBidiagUpper(R, b):
    dim = R.shape[0]
    x = np.zeros(dim)

    x[dim - 1] = b[dim - 1] / R[dim - 1, dim - 1]
    for i in range(dim - 2, -1, -1):
        x[i] = (b[i] - R[i, i + 1] * x[i + 1]) / R[i, i]

    return x

def SolveBidiagLower(L, y):
    dim = L.shape[0]
    x = np.zeros(dim)

    x[0] = y[0] / L[0, 0]
    for i in range(1, dim):
        x[i] = (y[i] - L[i, i - 1] * x[i - 1]) / L[i, i]

    return x

if __name__ == "__main__":
    A, b = citireDate("in.txt")
    

    L, R = FactorizeLR(A)


    y = SolveBidiagLower(L, b)
    

    x = SolveBidiagUpper(R, y)
    print("Solutia sistemului este: ")
    print("[ "+", ".join([str(round(e, 3)) for e in x]) + " ]")

