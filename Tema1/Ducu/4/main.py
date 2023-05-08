def calculeaza_polinom(x, v):
    rez = 0
    for i in range(len(v) - 1, -1, -1):
        rez += v[i]
        if i != 0:
            rez *= x

    return rez

print(calculeaza_polinom(3, [1, 2, 3, 4]))
