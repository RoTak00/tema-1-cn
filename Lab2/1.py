import numpy as np
import matplotlib.pyplot as plt 

def sgn(val):
    if val < 0:
        return -1
    elif val > 0:
        return 1
    return 0

relative_error = lambda prevx, x : abs((x - prevx) / x)

fun = lambda x : x**25 + 5* x**2 + 5 * x**3 + - 3

def Bisectie(f, a, b, eps = 10**-3):
    counter = 0
    xold = -1
    while True:
        x = a + (b - a) / 2

        if counter != 0 and relative_error(xold, x) < eps:
            return {'x':x, 'it':counter}

        if sgn(f(a)) != sgn(f(x)):
            b = x
        else:
            a = x
        
        counter += 1
        xold = x
    
if __name__ == '__main__':
    print(Bisectie(fun, 0, 6, 10**-5))

    fig = plt.figure(1)
    ax = plt.axes()

    x = np.linspace(0, 1.05, 100)
    y = fun(x)

    ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = f(x)')
    ax.grid(True, color = 'c')

    plt.xticks(np.arange(-4,4,1))
    plt.yticks(np.arange(-1.5,1.6,0.5))

    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Graph of f(x) = y')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')

    plt.show()

