import math

def f(x):
    return x * x * x

def deriv(fun, h, step, st, fin):
    res = {}
    i = st
    while i < fin:
        res[i] = ( (f(i + h) - f(i)) / h )
        i += step

    return res

file = open("file.out", "w")

res = deriv(f, 0.00000001, 0.01, -5, 5)
for key in res:
    print(f"f'({key}) = {res[key]}")
    file.write(f"{key},{res[key]}\n")
