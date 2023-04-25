import numpy as np
import matplotlib.pyplot as plt 

def sgn(val):
    if val < 0:
        return -1
    elif val > 0:
        return 1
    return 0

relative_error = lambda prevx, x : abs((x - prevx) / x)

fun = lambda x : x**3 - 7*x**2 + 14 * x - 6

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
    


    fig = plt.figure(1)
    ax = plt.axes()

    x = np.linspace(0, 4, 100)
    y = fun(x)

    ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = f(x)')

    ax.grid(True, color = 'c')

    plt.xticks(np.arange(-1,6,1))
    plt.yticks(np.arange(-7,5,1))

    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Graph of f(x) = y')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')

    print(Bisectie(fun, 0, 1, 10**-7)) # 0.5857
    print(Bisectie(fun, 2, 3.11, 10**-7)) # 3
    print(Bisectie(fun, 3.11, 4, 10**-7)) # 3.4142

    ax.axvline(x = 0.5857, color = 'r')
    ax.axvline(x = 3, color = 'r')
    ax.axvline(x = 3.4142, color = 'r')




    plt.show()

