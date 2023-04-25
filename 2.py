import math

def f(x):
    return x ** 3.25 - 23.2

def f2(x):
    return  x ** 2 - 5

def f3(x):
    return 100 * math.sin(x) - 32

def f4(x):
    return x - 5

def deriv(fun, p, h):
    res = ( (fun(p + h) - fun(p)) / h )

    return res

def approximate1(f, a, b, repeats):

    #maxIter = int(math.log2((b - a) / eps))
    maxIter = repeats

    results = []
    for i in range(maxIter):
        x = (a + b) / 2
        results.append({'a': a, 'b':b, 'x':x})

        if f(x) == 0:
            break

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    return results

def approximate2(f, a, b, repeats):
    point = a

    dp1 = deriv(f, (a+b)/4, 0.00001)
    dp2 = deriv(f, (a+b)*3/4, 0.00001)

    if dp1 > 0 and dp1 > dp2:
        point = a 
    if dp1 > 0 and dp1 < dp2:
        point = b
    
    if dp1 < 0 and dp1 > dp2:
        point = b
    if dp1 < 0 and dp1 < dp2:
        point = a

    results = []

    for i in range(repeats):
        point = point - (f(point) / deriv(f, point, 0.00000001))
        results.append({'x':point})
        if f(point) == 0:
            break

    return results

def approximate3(f, a, b, repeats):
    
    static = a
    if deriv(f, (a+b)/2, 0.0001) > 0:
        static = b
    results = []
    
    

    for i in range(repeats):
        results.append(0)

        results[i] = (static * f(results[i-1]) - f(static) * results[i-1]) / (f(static) - f(results[i-1]))

    return [{'x':el} for el in results] 


results = approximate2(f2, 1, 6, 50)
    
for index, item in enumerate(results):
    val = item['x']
    print(f'Iter {index}: x = {val}')