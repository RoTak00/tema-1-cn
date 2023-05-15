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

def VerificarePatratica(A, tol = 10 ** -16):
    # Verificam ca A sa fie matrice bidimensionala
    if A.ndim != 2:
        print("Vectorul nu este bidimensional")
        return False

    # Verificam ca A sa fie matrice patratica
    if A.shape[0] != A.shape[1]:
        print("Matricea nu este patratica")
        return False
    
    return True

def readLinearSystem(path):
    dim = 0
    mat = ""
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [float(x) for x in file.readline().split()]

    return mat[:, :dim], mat[:, dim:].T[0]

def Invert(A, tol = 10 ** -16):
    # Verificam ca datele introduse sunt corecte
    if VerificarePatratica(A, tol) == False:
        return None, None
    
   
    
    # Dimensiunea sistemului
    n = A.shape[0]

    Ainv = np.identity(n)
    for k in range(n):
        
        # Aflam prima linie pe care Apk este nenul
        p = k
        while p < n and abs(A[p][k]) < tol:
            p += 1

        # Daca nu exista Apk nenul, sistemul nu e determinat
        if abs(A[p][k]) < tol:
            print("Sistemul nu este determinat")
            return None, None

        # Daca apk nu e de forma akk, interschimbam liniile
        if k != p:
            A[[k, p]] = A[[p, k]]
            Ainv[[k, p]] = Ainv[[p, k]]

        # Reducem liniile pentru a forma matricea diagonala
        for l in range(n):
            if l == k:
                continue
            m = A[l][k] / A[k][k]
            A[l] = A[l] - A[k] * m
            Ainv[l] = Ainv[l] - Ainv[k] * m
    
    # Daca matricea nu e corecta, sistemul nu e determinat
    if abs(A[n-1][n-1]) < tol:
        print("Sistemul nu este determinat")
        return None, None
    
    det = 1
    # transformam A in mat identitate
    for l in range(n):
            det *= A[l][l]
            Ainv[l] = Ainv[l] / A[l][l]

    return Ainv, det

def Multiply(v, A):
    res = np.zeros(v.shape)
    
    for i in range(len(res)):
        for j in range(len(res)):
            res[i] += v[j] * A[i][j]

    return res 
if __name__ == "__main__":
    A, b = readLinearSystem("in.txt")
    Ainv, det = Invert(A)

    if Ainv is not None:
        print("Inversa sistemului: ")
        print(Ainv)
    else:
        print("Sistemul nu are invers ")

    if det is not None:
        print("Determinantul sistemului: ")
        print(det)
    else:
        print("Sistemul are determinantul 0")

    if Ainv is not None:
        res = Multiply(b, Ainv)

        print("Sistemul are solutia:")
        print(res)