import numpy as np

def readMat(path):
    dim = 0
    with open(path, 'r') as file:
        dim = int(file.readline())
        mat = np.zeros((dim, dim+1))
    
        for i in range(dim):
            mat[i] = [int(x) for x in file.readline().split()]

    return mat

def rowSub(line1, line2, mult):
    for i in range(len(line1)):
        line1[i] -= line2[i] * mult
    return line1

def GaussElim(mat):
    n = len(mat)
    for k in range(n-1):

        p = list(mat[:, k]).index(max(mat[:, k]))

        if mat[p][k] == 0:
            print("eroare 1")
            return -1

        if k != p:
            mat[[k, p]] = mat[[p, k]]

        for l in range(k + 1, n):
            m = mat[l][k] / mat[k][k]
            mat[l] = rowSub(mat[l], mat[k], m)
    
    if mat[n - 1][n - 1] == 0:
        print("eroare 2")
        return -1
    
    return mat


def Solve(mat):
    n = len(mat)
    b = mat[:, n]
    res = [0 for x in range(n)]

    for k in reversed(range(0, n)):
        t = b[k]
        for j in range(k + 1, n):
            t -= mat[k][j] * res[j]

        t /= mat[k][k]
        res[k] = t
    return res


if __name__ == '__main__':
    mat = readMat("in.txt")
    print(mat)
    mat = GaussElim(mat)
    print("After transformation:")
    print(mat)
    res = Solve(mat)
    print("After solving:")
    print(res)

