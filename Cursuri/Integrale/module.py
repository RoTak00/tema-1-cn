import math
import numpy as np

fun = lambda x: math.log(x + 1) * math.exp(2 * x)

def integrala_dreptunghi(f, a, b, n):
    x = np.linspace(a, b, n)
    res = 0
    for i in range(n - 1):
        a = x[i]
        b = x[i + 1]
        int_part = (b - a) * f ((a + b) / 2)
        res += int_part

    return res

def integrala_trapez(f, a, b, n):
    x = np.linspace(a, b, n)
    res = 0
    for i in range(n - 1):
        a = x[i]
        b = x[i + 1]
        int_part = (b - a) / 2 * (f(a) + f(b))
        res += int_part

    return res

def integrala_simpson(f, a, b, n):
    x = np.linspace(a, b, n)
    res = 0
    for i in range(n - 1):
        a = x[i]
        b = x[i + 1]
        int_part = (b - a) / 6 * (f(a) + 4 * f ((a + b) / 2) + f(b))
        res += int_part

    return res

if __name__ == "__main__":
    print("Precizie mica (trapez dreptunghi simpson)")
    print(integrala_trapez(fun, 0, 1, 3))
    print(integrala_dreptunghi(fun, 0, 1, 3))
    print(integrala_simpson(fun, 0, 1, 3))

    print("Precizie medie (trapez dreptunghi simpson)")
    print(integrala_trapez(fun, 0, 1, 100))
    print(integrala_dreptunghi(fun, 0, 1, 100))
    print(integrala_simpson(fun, 0, 1, 100))

    print("Precizie mare (trapez dreptunghi simpson)")
    print(integrala_trapez(fun, 0, 1, 1000))
    print(integrala_dreptunghi(fun, 0, 1, 1000))
    print(integrala_simpson(fun, 0, 1, 1000))