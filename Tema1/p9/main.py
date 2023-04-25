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

def readLinearSystem(path):
    dim = 0
    mat = ""
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [float(x) for x in file.readline().split()]

    return mat[:, :dim], mat[:, dim:].T[0]

def GaussJordan(A, b, tol = 10 ** -16):
    # Verificam ca datele introduse sunt corecte
    if Verificare(A, b, tol) == False:
        return None
    
    # Construim matricea extinsa
    Aext = np.c_[A, b]

    # Dimensiunea sistemului
    n = A.shape[0]

    for k in range(n):
        
        # Aflam prima linie pe care Apk este nenul
        p = k
        while p < n and abs(Aext[p][k]) < tol:
            p += 1

        # Daca nu exista Apk nenul, sistemul nu e determinat
        if abs(Aext[p][k]) < tol:
            print("Sistemul nu este determinat")
            return None

        # Daca apk nu e de forma akk, interschimbam liniile
        if k != p:
            Aext[[k, p]] = Aext[[p, k]]

        # Reducem liniile pentru a forma matricea triunghiulara
        for l in range(n):
            if l == k:
                continue
            m = Aext[l][k] / Aext[k][k]
            Aext[l] = Aext[l] - Aext[k] * m
    
    # Daca matricea nu e corecta, sistemul nu e determinat
    if abs(Aext[n-1][n-1]) < tol:
        print("Sistemul nu este determinat")
        return None

    return Aext

def SolveDiag(diag):
    dim = diag.shape[0]
    res = np.zeros(dim)
    for i in range(dim):
        res[i] = diag[i][dim] / diag[i][i]
    return res

if __name__ == "__main__":
    A, b = readLinearSystem("in.txt")
    Diag = GaussJordan(A, b)
    print(Diag)
    res = SolveDiag(Diag)
    print(res)