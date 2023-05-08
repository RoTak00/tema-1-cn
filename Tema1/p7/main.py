import math
import numpy as np
import matplotlib.pyplot as plt

fun2 = lambda x : math.sin(x) - (math.e ** (-x))
fun= lambda x : 2 * x + 3 * math.cos(2 * x)
relative_error = lambda prevx, x : abs((x - prevx) / x)

def Secanta(f, x0, x1, a, b, eps = 10**-5):
    if f(a) * f(b) > 0:
        return None
    
    vx = [x0, x1]
    k = 1

    while relative_error(vx[k-1], vx[k]) >= eps:
        k += 1
        xk = (vx[k-2] * f(vx[k-1]) - vx[k-1] * f(vx[k-2])) / (f(vx[k-1]) - f(vx[k-2]))
        vx.append(xk)

        if xk < a or xk > b:
            return None
    
    return {'x': vx[k], 'nr_it': k - 1}

def PozitieFalsa(f, _a, _b, eps = 10**-5):

    if f(_a) * f(_b) > 0:
        return None
    
    k = 0
    a = [_a]
    b = [_b]
    x = [(_a*f(_b) - _b * f(_a)) / (f(_b) - f(_a))]

    k = 0

    while k == 0 or relative_error(x[k-1], x[k]) >= eps:
        k += 1
        if f(x[k-1]) == 0:
            x.append(x[k-1])
            break

        elif f(a[k-1])*f(x[k-1]) < 0:
            a.append(a[k-1])
            b.append(x[k-1])
            x.append((a[k]*f(b[k]) - b[k] * f(a[k])) / (f(b[k]) - f(a[k])))
        else:
            a.append(x[k-1])
            b.append(b[k-1])
            x.append((a[k]*f(b[k]) - b[k] * f(a[k])) / (f(b[k]) - f(a[k])))

    return {'x': x[k], 'nr_it': k}
                      
if __name__ == '__main__':
    
    result_points1 = []
    result_points2 = []
    start_interval = -2
    end_interval = 3
    jump_interval = 0.01

    for i in np.linspace(start_interval, end_interval, (int)((end_interval - start_interval) / jump_interval)):
        
        pt1 = Secanta(fun, i, i + jump_interval, i, i + jump_interval, 10**-5)
        if pt1:
            result_points1.append(pt1)

        pt2 = PozitieFalsa(fun, i, i + jump_interval, 10**-5)
        if pt2:
            result_points2.append(pt2)

    print("Metoda Secantei:")
    print(result_points1)

    print("Metoda Pozitiei False:")
    print(result_points2)


    fig = plt.figure(1)
    ax = plt.axes()
    x = np.linspace(start_interval, end_interval, (end_interval - start_interval) * 50)
    y = np.vectorize(fun)(x)
    ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = f(x)')
    ax.scatter([x['x'] for x in result_points1], np.zeros(len(result_points1)), color="r")
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