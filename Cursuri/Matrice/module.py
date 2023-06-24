import numpy as np

def FactorizareLUFaraPivotare(A):
    dim = A.shape[0]
    L = np.eye(dim)  # Initialize L as the identity matrix
    P = np.eye(dim)  # Initialize P as the identity matrix
    U = np.copy(A)  # Initialize U as a copy of A

    for k in range(dim-1):
        p = k
        while U[p, k] == 0 and p < dim - 1:
            p += 1
        if p == dim - 1:
            print("Nu se poate")
            return None, None, None
        if p != k:
            U[[k, p], :] = U[[p, k], :]
            L[[k, p], :] = L[[p, k], :]
            P[[k, p], :] = P[[p, k], :]

        for i in range(k+1, dim):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U


def FactorizareLUPivotarePartiala(A):
    dim = A.shape[0]
    L = np.eye(dim)  # Initialize L as the identity matrix
    U = np.copy(A)  # Initialize U as a copy of A
    P = np.eye(dim)  # Initialize P as the identity matrix

    for k in range(dim-1):
        # Partial Pivoting
        max_row = np.argmax(np.abs(U[k:, k])) + k
        if max_row != k:
            U[[k, max_row], k:] = U[[max_row, k], k:]
            P[[k, max_row], :] = P[[max_row, k], :]
            if k >= 1:
                L[[k, max_row], :k] = L[[max_row, k], :k]

        if U[k, k] == 0:
            print("Nu se poate")
            return None, None, None

        for i in range(k+1, dim):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U


def DescompunereCholesky(A):
    # Check if the input matrix is square
    if A.shape[0] != A.shape[1]:
        print("Input matrix is not square.")
        return None
    
    # Check if the input matrix is symmetric
    if not np.allclose(A, A.T):
        print("Input matrix is not symmetric.")
        return None
    
    # Check if the input matrix is positive definite
    if not np.all(np.linalg.eigvals(A) > 0):
        print("Input matrix is not positive definite.")
        return None
    
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                sum_term = np.sum(L[i, :j] ** 2)
                L[i, j] = np.sqrt(A[i, i] - sum_term)
            else:
                sum_term = np.sum(L[i, :j] * L[j, :j])
                L[i, j] = (A[i, j] - sum_term) / L[j, j]

    return L

if __name__ == "__main__":
    A = np.array([[4, 2, -2],
              [2, 5, -4],
              [-2, -4, 11]], float)
    L = cholesky_decomposition(A)
    if L is not None:
        print(L)
        print(L.T)