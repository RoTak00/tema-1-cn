import numpy as np
import math

def readMat(path):
    dim = 0
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [int(x) for x in file.readline().split()]

    return mat


def GaussElim(mat):

    n = len(mat)
    ind = np.arange(0, n, 1)
    for k in range(n-1):

        p, m = k, k

        for i in range(k, n-1):
            for j in range(k, n-1):
                if math.fabs(mat[i][j]) > math.fabs(mat[p][m]):
                    p, m = i, j

        if mat[p][k] == 0:
            print("eroare 1")
            return -1, -1

        if k != p:
            mat[[k, p]] = mat[[p, k]]

        if k != m:
            mat[:, [k, m]] = mat[:, [m, k]]
            t = ind[k]
            ind[k] = ind[m]
            ind[m] = t

        for l in range(k + 1, n):
            m = mat[l][k] / mat[k][k]
            mat[l] -= mat[k] * m
    
    if mat[n - 1][n - 1] == 0:
        print("eroare 2")
        return -1, -1
    
    return mat, ind


def Solve(mat, ind):
    n = len(mat)
    b = mat[:, n]
    res = [0 for x in range(n)]

    for k in reversed(range(0, n)):
        t = b[k]
        for j in range(k + 1, n):
            t -= mat[k][j] * res[j]

        t /= mat[k][k]
        res[k] = t

    res2 = [res[ind[x]] for x in range(n)]
    return res2


if __name__ == '__main__':
    mat = readMat("in.txt")
    print(mat)
    mat, ind = GaussElim(mat)
    if type(mat) is int:
        print("Sistemul nu este determinat")
        exit()

    print("After transformation:")
    print(mat)
    res = Solve(mat, ind)
    print("After solving:")
    print(res)

