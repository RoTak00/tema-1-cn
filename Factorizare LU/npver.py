import numpy as np
import sys
sys.path.append("../")
import module as myla
import scipy.linalg as la

if __name__ == '__main__':
    A, b = myla.readLinearSystem("in.txt")
    P, L, U = la.lu(A)

    y = myla.SubsDesc(U, b)

    for i in range(len(A))
    res = myla.SubsAsc(L, y)

    res2 = np.linalg.solve(A, b)


    print(res)
    print(res2)
    