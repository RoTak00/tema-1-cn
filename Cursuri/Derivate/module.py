import numpy as np
import math

fun = lambda x : x**3 - 7*x**2 + 14 * x - 6
df = lambda x : 3*x**2 - 14*x+14
df2 = lambda x : 6*x - 14

# DERIVATE DE ORDINUL I
def diferenta_finita_progresiva(f, x, eps = 10**-5):
    return (f(x + eps) - f(x)) / eps

def diferenta_finita_regresiva(f, x, eps = 10**-5):
    return (f(x) - f(x - eps)) / eps

def diferenta_finita_centrata(f, x, eps = 10**-5):
    return (f(x + eps) - f(x - eps)) / (2 * eps)

def extrapolare_richardson(f, x, prec = 3, eps = 10**-5):
    dim = prec + 1

    Q = np.zeros((dim, dim))

    for i in range(dim):
        Q[i][0] = diferenta_finita_progresiva(f, x, eps / (2 ** i))

    for i in range(1, dim):
        for j in range(1, i + 1):
            Q[i][j] = Q[i,j-1] + (Q[i,j-1] - Q[i-1][j-1]) / (2 ** j - 1)

    return Q[dim - 1][dim - 1]


# DERIVATE DE ORDINUL II

def derivata_2(f, x, eps = 10**-5):
    return (f(x + eps) - 2 * f(x) + f(x - eps)) / eps**2


# da valori bune doar pentru precizii mai mari de ~40
def extrapolare_richardson_2(f, x, prec = 45, eps = 10**-5):
    dim = prec + 1

    Q = np.zeros((dim, dim))

    for i in range(dim):
        Q[i][0] = derivata_2(f, x, eps / (2 ** i))

    for i in range(1, dim - 1):
        for j in range(1, i + 1):
            Q[i][j] = Q[i,j-1] + (Q[i,j-1] - Q[i-1][j-1]) / (2 ** j - 1)

    return Q[dim - 2][dim - 2]

    
if __name__ == "__main__":
    # bad_eps = 0.5
    # print("progresiva eps .5")
    # print(diferenta_finita_progresiva(fun, 2, bad_eps))
    # print("regresiva eps .5")
    # print(diferenta_finita_regresiva(fun, 2, bad_eps))
    # print("centrata eps .5")
    # print(diferenta_finita_centrata(fun, 2, bad_eps))
    # print("richardson eps .5 prec 1")
    # print(extrapolare_richardson(fun, 2, prec = 1, eps = bad_eps))
    # print("richardson eps .5 prec 5")
    # print(extrapolare_richardson(fun, 2, prec = 5, eps = bad_eps))
    # print("richardson eps .5 prec 10")
    # print(extrapolare_richardson(fun, 2, prec = 10, eps = bad_eps))
    # print("richardson eps .5 prec 15")
    # print(extrapolare_richardson(fun, 2, prec = 15, eps = bad_eps))
    # print("richardson eps .5 prec 20")
    # print(extrapolare_richardson(fun, 2, prec = 20, eps = bad_eps))

    print(derivata_2(fun, 2))

    for i in range(1, 50):
        print(f"richardson eps .5 prec {i}")
        print(extrapolare_richardson(fun, 2, prec = i, eps = 10**-5))


