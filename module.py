import numpy as np

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

def SubsDesc(A, b, tol = 10 ** -16):
    if Verificare(A, b, tol) == False:
        return None

    n = A.shape[0]

    # Verificam ca A sa fie superior triunghiulara
    for i in range(n):
        for j in range(i):
            if abs(A[i][j]) > tol:
                print("Matricea nu e superior triunghiulara")
                return None
    # Verificam ca sistemul sa fie compatibil determinat
    for i in range(n):
        if abs(A[i][i]) < tol:
                print("Sistemul nu e determinat")
                return None         

    # Calculam rezultatul sistemului
    res = np.zeros(n)
    for k in reversed(range(n)):
        t = b[k]
        for j in range(k + 1, n):
            t -= A[k][j] * res[j]

        t /= A[k][k]
        res[k] = t
    return res
    
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

def readMatrix(path):
    n = 0
    m = 0

    with open(path, 'r') as file:
        n, m = [int(x) for x in file.readline().split()]
        mat = np.zeros((n, m))

        for i in range(n):
            mat[i] = [float(x) for x in file.readline().split()]
    
    return mat

def readLinearSystem(path):
    dim = 0
    mat = ""
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [float(x) for x in file.readline().split()]

    return mat[:, :dim], mat[:, dim:].T[0]
