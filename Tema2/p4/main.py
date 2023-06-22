import numpy as np

def readSymMatrix(path):
    A = []
    va = []

    with open(path, 'r') as file:
        va = np.array([float(x) for x in file.readline().split()])
    
    
    dim = va.shape[0]
    print(dim)
    A = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim - i):
            A[j+i, j] = va[i]
            A[j, j + i] = va[i]

    return A, va

# A function that performs Cholesky factorization on a matrix



if __name__ == "__main__":
    A, va = readSymMatrix("in.txt")
    print(A)

    print(np.linalg.cholesky(A))