import math

def approximate1(f, a, b, eps):

    maxIter = int(math.log2((b - a) / eps))

    results = []
    while True:
        x = (a + b) / 2
        results.append({'a': a, 'b':b, 'x':x})

        if len(results) > 2:
            er = abs(results[-1]['x'] - results[-2]['x']) / abs(results[-2]['x'])
            print(er)
            if er < eps:
                break

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    

    return results

def f(x):
    return x*x*x - 7 * x *x + 14 *x - 6

if __name__ == '__main__':
    print(approximate1(f, 0, 1, 0.00001))