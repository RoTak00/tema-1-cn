import numpy as np
import matplotlib.pyplot as plt
import math

PI = 3.1415

def sortFun(el):
    return el[0]
def fun(px, n, x, a, b):
    for i in range(n):
        if x[i] <= px <= x[i+1]:
            return a[i] + b[i] * (px - x[i])
    return 0


def SplineL(X, Y, x):
    n = len(X)
    
    slopes = []
    for i in range(n - 1):
        slopes.append((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]))

    ind = 0
    while ind < n - 1 and x > X[ind + 1]:
        ind += 1
    
    return Y[ind] + (slopes[ind] * (x - X[ind]))

def SplineLVector(X, Y, vx):
    n = len(X)

    slopes = []
    for i in range(n - 1):
        slopes.append((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]))

    result = []
    for x in vx:
        ind = 0
        while ind < n - 1 and x > X[ind + 1]:
            ind += 1
        
        result.append(Y[ind] + (slopes[ind] * (x - X[ind])))
    
    return result
    

if __name__ == "__main__":

    N = 4
    left = -PI/2
    right = PI/2


    X = np.linspace(left, right, N + 1)
    Y = np.array([math.sin(x) for x in X])

    plot_x = np.linspace(left, right, 100)
    plot_y = [SplineL(X, Y, x) for x in plot_x]



    fig = plt.figure(1)
    ax = plt.axes()


    ax.plot(plot_x, plot_y, linestyle='-', lw = 2, color = 'b', label = 'Interpolarea Spline a functiei')
    ax.plot(plot_x, np.vectorize(math.sin)(plot_x), linestyle = '--', lw = 1, color = 'r', label = "Functia Sin")
    ax.scatter(X, Y, color = 'r', label = "Nodurile de interpolare")


    ax.grid(True, color = 'c')


    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Interpolare Liniara')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')

    plt.show()