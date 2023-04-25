import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

relative_error = lambda prevx, x : abs((x - prevx) / x)

fun = lambda x : x**3 - 7*x**2 + 14 * x - 6
#fun = lambda x : np.sin(x) * np.cos(x ** x) - np.tan(x)

def Bisectie(f, a, b, eps = 10**-3, out_ptable = None):
    counter = 0
    xold = -1
    
    # Daca din start valorile sunt pe aceeasi parte a axei Ox, ori nu avem o radacina, ori avem mai multe.
    # it's not good either way, returnam none
    if f(a) * f(b) > 0:
        return None
    
    while True:
        x = a + (b - a) / 2

        # adaugam datele la PrettyTable, daca acesta exista
        if out_ptable != None:
            y = fun(x)
            err = relative_error(xold, x) if counter != 0 else 'nil'
            log = (float)(b - a) / (2 ** (counter))

            out_ptable.add_row([counter + 1, x, y, err, log])

        if counter != 0 and relative_error(xold, x) < eps:
            return {'x':x, 'it':counter}

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        
        counter += 1
        xold = x
    
if __name__ == '__main__':
    
    result_points = []
    result_tables = []
    start_interval = 0
    end_interval = 4
    jump_interval = 0.05

    for i in np.linspace(start_interval, end_interval, (int)((end_interval - start_interval) / jump_interval)):
        table = PrettyTable(['k', 'x_k', 'f(x_k)', 'rel err', '(b-a)/2^(k-1)'])
        pt = Bisectie(fun, i, i + jump_interval, 10**-6, table)
        if pt:
            result_points.append(pt['x'])
            result_tables.append(table)

    print(result_points)

    for table in result_tables:
        print(table)

    fig = plt.figure(1)
    ax = plt.axes()

    x = np.linspace(start_interval, end_interval, (end_interval - start_interval) * 50)
    y = fun(x)

    ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = f(x)')

    ax.scatter(result_points, np.zeros(len(result_points)), color="r")
    ax.grid(True, color = 'c')

    plt.xticks(np.arange(start_interval,end_interval,(int)((end_interval - start_interval) / 4)))
    plt.yticks(np.arange(min(y),max(y),(int)((end_interval - start_interval) / 4)))

    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Graph of f(x) = y')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')


    




    plt.show()
