import math
import numpy as np

fun = lambda x : math.sin(x) - (math.e ** (-x))
relative_error = lambda prevx, x : abs((x - prevx) / x)

def Secanta(f, a, b, eps = 10**-3, xold = -1, it = 0):
    print(a, b, f(a), f(b))
    if fun(a) * fun(b) > 0:
        return None
    
    if fun(a) > 0:
        xnew = a - (f(a) / (f(b) - f(a))) * (b - a)

        if xold != -1 and relative_error(xold, xnew) < eps:
            return {'x': xnew, 'it': it}
        
        return Secanta(f, xnew, b, eps, a, it + 1)
    
    if fun(a) < 0:
        xnew = b - (f(b) / (f(b) - f(a))) * (b - a)

        if xold != -1 and relative_error(xold, xnew) < eps:
            return {'x': xnew, 'it': it}
        
        return Secanta(f, xnew, b, eps, a, it + 1)




if __name__ == '__main__':
    
    result_points = []
    start_interval = 0
    end_interval = 10
    jump_interval = 0.05

    for i in np.linspace(start_interval, end_interval, (int)((end_interval - start_interval) / jump_interval)):
        print("For: ", i, i + jump_interval)
        pt = Secanta(fun, i, i + jump_interval, 10**-5)
        if pt:
            print(i, i + jump_interval)
            result_points.append(pt['x'])

    print(result_points)