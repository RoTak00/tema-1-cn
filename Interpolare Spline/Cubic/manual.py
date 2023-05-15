import numpy as np
import matplotlib.pyplot as plt

def SplineCubica(X, Y, derivata_fun_a, derivata_fun_b, vx):
    dim = len(X) - 1
    Mat = np.zeros((dim + 1, dim + 1))
    Mat[0][0] = 1
    Mat[dim][dim] = 1
    for i in range(1, dim):
        Mat[i][i] = 4
        Mat[i][i - 1] = 1
        Mat[i][i + 1] = 1
    
    H = np.zeros(dim)
    for i in range(dim):
        H[i] = X[i + 1] - X[i]
    
    W = np.zeros(dim + 1)
    W[0] = derivata_fun_a
    W[dim] = derivata_fun_b
    for i in range(1, dim):
        W[i] = (3 / H[i]) * (Y[i + 1] - Y[i - 1])
    B = np.linalg.solve(Mat, W)

    A = np.zeros(dim)
    C = np.zeros(dim)
    D = np.zeros(dim)

    for i in range(dim):
        A[i] = Y[i]
        C[i] = (3 / (H[i] * H[i])) * (Y[i + 1] - Y[i]) - (B[i + 1] + 2 * B[i]) / H[i]
        D[i] = (-2 / (H[i]**3)) * (Y[i + 1] - Y[i]) + (B[i + 1] + B[i]) / (H[i]**2)


    for j in range(dim):
        if (vx >= X[j]) and (vx <= X[j + 1]):
            S = A[j] + B[j] * (vx - X[j]) + C[j] * ((vx-X[j]) ** 2) + D[j] * ((vx-X[j])**3)

    return S
        

def rezolva(x, X, a, b, c, d):
    v = x - X
    return a + b * v + c * v * v +  d * v * v* v

if __name__ == '__main__':
    a = -1
    b = 1
    
    q = int(input("Functie sau puncte? [0 - functie, 1 - puncte] "))

    x = []
    y = []
    f = ""
    if q == 0:
        divs = int(input("diviziuni? 2 -> "))
        x = np.linspace(a, b, divs)
        f = lambda x : 1 / (1 + 25 * x*x)
        df = lambda x : (-1 / (((1 + 25 *x * x)**2))) * 50 * x
        dfa = df(a)
        dfb = df(b)
        y = f(x)

    elif q == 1:
        print("Cate puncte?: ")
        n = int(input())

        x = np.zeros(n)
        for i in range(n):
            x[i] = float(input("x"+str(i + 1) + " "))

        y = np.zeros(n)
        for i in range(n):
            y[i] = float(input("y"+str(i + 1) + " "))

        a = min(x)
        b = max(x)
        print(a)
        print(b)
        dfa = 0
        dfb = 0

    prec = min(int(input("Precizie? 1 - 50 ")), 50)
    prec *= 100
    print(y)
    px = np.linspace(a, b, prec)
    py = np.zeros(prec)
    for i, vx in enumerate(px):
        py[i] = SplineCubica(x, y, dfa, dfb, vx)
    

    fig = plt.figure(1)
    ax = plt.axes()

    cols = {0: 'b', 1: 'g', 2: 'r'}

    if q == 0:
        ax.plot(px, f(px) , linestyle='--', lw = 2, color = 'b', label = 'f(x) = y')
    ax.plot(px, py, linestyle='-', lw = 2, color = 'g', label = 'P(x) = y')

    ax.scatter(x, y, color = 'b', label = "X, Y")

    ax.grid(True, color = 'c')


    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Interpolare Spline Cubica')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')

    plt.show()
