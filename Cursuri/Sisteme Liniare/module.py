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

def GaussFaraPiv(A, b, tol = 10 ** -16):
    # Verificam ca datele introduse sunt corecte
    if Verificare(A, b, tol) == False:
        return None
    
    # Construim matricea extinsa
    Aext = np.c_[A, b]

    # Dimensiunea sistemului
    n = A.shape[0]

    for k in range(n - 1):
        
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
        for l in range(k + 1, n):
            m = Aext[l][k] / Aext[k][k]
            Aext[l] = Aext[l] - Aext[k] * m
    
    # Daca matricea nu e corecta, sistemul nu e determinat
    if abs(Aext[n-1][n-1]) < tol:
        print("Sistemul nu este determinat")
        return None

    # Rezolvam sistemul rezultant prin substitutie descendenta
    return SubsDesc(Aext[:, :n], Aext[:, n:].T[0], tol)

def GaussPivPart(A, b, tol = 10 ** -16):
    # Verificam ca datele introduse sunt corecte
    if Verificare(A, b, tol) == False:
        return None
    
    # Construim matricea extinsa
    Aext = np.c_[A, b]

    # Dimensiunea sistemului
    n = A.shape[0]

    for k in range(n - 1):
        
        # Aflam prima linie pe care Apk este nenul
        p = k

        # Gasim linia cu cel mai mare apk
        for i in range(k + 1, n):
            if abs(Aext[i][k]) > abs(Aext[p][k]):
                p = i
        #print(A)
        # Daca nu exista Apk nenul, sistemul nu e determinat
        if abs(Aext[p][k]) < tol:
            print("Sistemul nu este determinat")
            return None

        # Daca apk nu e de forma akk, interschimbam liniile
        if k != p:
            Aext[[k, p]] = Aext[[p, k]]

        # Reducem liniile pentru a forma matricea triunghiulara
        for l in range(k + 1, n):
            m = Aext[l][k] / Aext[k][k]
            Aext[l] = Aext[l] - Aext[k] * m
    
    # Daca matricea nu e corecta, sistemul nu e determinat
    if abs(Aext[n-1][n-1]) < tol:
        print("Sistemul nu este determinat")
        return None

    # Rezolvam sistemul rezultant prin substitutie descendenta
    return SubsDesc(Aext[:, :n], Aext[:, n:].T[0], tol)

def GaussPivTotala(A, b, tol = 10 ** -16):
    # Verificam ca datele introduse sunt corecte
    if Verificare(A, b, tol) == False:
        return None
    
    # Construim matricea extinsa
    Aext = np.c_[A, b]

    Ind = [x for x in range(A.shape[0])]

    # Dimensiunea sistemului
    n = A.shape[0]

    for k in range(n - 1):
        
        p = k
        o = k

        # Gasim linia cu cel mai mare apk
        for i in range(k, n):
            for j in range(k, n):
                if abs(Aext[i][j]) > abs(Aext[p][o]):
                    p = i
                    o = j
        #print(A)
        # Daca nu exista Apk nenul, sistemul nu e determinat
        if abs(Aext[p][o]) < tol:
            print("Sistemul nu este determinat")
            return None

        # Daca apk nu e de forma akk, interschimbam liniile
        if k != p:
            Aext[[k, p]] = Aext[[p, k]]
        if k != o:
            Aext[:, [k, o]] = Aext[:, [o, k]]
            Ind[k], Ind[o] = Ind[o], Ind[k]


        # Reducem liniile pentru a forma matricea triunghiulara
        for l in range(k + 1, n):
            m = Aext[l][k] / Aext[k][k]
            Aext[l] = Aext[l] - Aext[k] * m
    
    # Daca matricea nu e corecta, sistemul nu e determinat
    if abs(Aext[n-1][n-1]) < tol:
        print("Sistemul nu este determinat")
        return None

    # Rezolvam sistemul rezultant prin substitutie descendenta
    
    rez = SubsDesc(Aext[:, :n], Aext[:, n:].T[0], tol)

    rez = [rez[i] for i in Ind]
    return rez


def readLinearSystem(path):
    dim = 0
    mat = ""
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [float(x) for x in file.readline().split()]

    return mat[:, :dim], mat[:, dim:].T[0]

if __name__ == "__main__":
    A, b = readLinearSystem("in.txt")
    print(GaussPivTotala(A, b, 10**-10))
