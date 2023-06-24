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

if __name__ == "__main__":
    A = np.array([[0, 1, 3], [1, 0, 6], [7, 8, 9]], float)
    P, L, U = FactorizareLUFaraPivotare(A)
    print(P)
    print(L)
    print(U)