import npver as np
import sys
sys.path.append("../")
import module as myla

def LUFactGPP(A):
    n = len(A)
    L = np.identity(n)
    w = np.arange(0, n)

    for k in range(n - 1):
        p = k
        for j in range(k, n):
            if A[j,k] > A[p,k]:
                p = j


        if A[p, k] == 0:
            print("Error")
            return None
        
        if p != k:
            A[[p, k]] = A[[k, p]]
            w[p], w[k] = w[k], w[p]
            if k > 1:
                for j in range(k - 1):
                    L[p, j], L[k, j] = L[k, j], L[p, j]
        
        for l in range(k + 1, n):
            L[l,k] = A[l, k] / A[k, k]
            A[l] = A[l] - A[k] * L[l, k]

    if A[n - 1][n - 1] == 0:
        print("Error")
        return None
    
    U = A[:]
    return {"L": L, "U": U, "w": w} 

if __name__ == '__main__':
    A, b = myla.readLinearSystem("in.txt")