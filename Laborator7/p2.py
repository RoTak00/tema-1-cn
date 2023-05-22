import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define Richardson procedure
def Richardson(f, x, h, n):
    """
    This function performs Richardson extrapolation on a given function f, at a given point x, with a given step size h,
    and a given number of steps n. It returns an estimate of the value of the function at x obtained from the extrapolation.
    :param f: The function to be extrapolated.
    :param x: The point at which the extrapolation is performed.
    :param h: The initial step size.
    :param n: The number of steps to take in the extrapolation.
    :return: An estimate of the value of the function at x obtained from the extrapolation.
    """
    phi = lambda x, h: (f(x + h) - f(x)) / h

    Q = np.zeros((n,n))
    for i in range(n):
        Q[i,0] = phi(x, h / (2 ** i))
    
    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = Q[i,j-1] + 1/(2 ** j - 1) * (Q[i, j-1] - Q[i-1, j-1])
    
    return Q[n-1,n-1]

if __name__ == "__main__":
    f = lambda x : (1/(1 + 25*x**2))
    a = -1
    b = 1

    x_grafic = np.linspace(a, b, 100)
    n1 = 1
    n2 = 2
    n3 = 4

    h = (b - a) / (len(x_grafic) - 1)

    df1 = np.zeros(len(x_grafic))
    df2 = np.zeros(len(x_grafic))
    df3 = np.zeros(len(x_grafic))

    for i in range(len(x_grafic)):
        df1[i] = Richardson(f, x_grafic[i], h, n1)
        df2[i] = Richardson(f, x_grafic[i], h, n2)
        df3[i] = Richardson(f, x_grafic[i], h, n3)
    
    fig, ax = plt.subplots(2)


    ax[0].plot(x_grafic, df1, label = "n = 1")
    ax[0].plot(x_grafic, df2, label = "n = 2")
    ax[0].plot(x_grafic, df3, label = "n = 4")



    a = sp.Symbol("a")
    df_exp = sp.diff((1 / (1 + 25 * a * a)), a)
    df_func = sp.lambdify((a), df_exp, "numpy")
    df = df_func(x_grafic)

    ax[1].plot(x_grafic, np.abs(df - df1), label = "n = 1")
    ax[1].plot(x_grafic, np.abs(df - df2), label = "n = 2")
    ax[1].plot(x_grafic, np.abs(df - df3), label = "n = 4")

    plt.show()
