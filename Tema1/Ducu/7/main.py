import math
import numpy as np
import matplotlib.pyplot as plt

def eroare(x1, x2):
    if x2 == 0:
        return 1
    return abs((x2 - x1) / x2)

def functie(x):
    return 2 * x + 3 * math.cos(2 * x)

def Secanta(f, x0, x1, eps = 0.00001):
    v = [x0, x1]
    k = 1

    while eroare(v[k-1], v[k]) >= eps:
        k += 1
        xk = (v[k-2] * f(v[k-1]) - v[k-1] * f(v[k-2])) / (f(v[k-1]) - f(v[k-2]))
        v.append(xk)
    
    return {'x': v[k], 'it': k - 1}

def PozitieFalsa(f, a, b, eps = 0.00005):
    k = 0
    va = [a]
    vb = [b]
    x = [(a*f(b) - b * f(a)) / (f(b) - f(a))]

    k = 0

    while k == 0 or eroare(x[k-1], x[k]) >= eps:
        k += 1
        if f(x[k-1]) == 0:
            x.append(x[k-1])
            break

        elif f(va[k-1])*f(x[k-1]) < 0:
            va.append(va[k-1])
            vb.append(x[k-1])
            x.append((va[k]*f(vb[k]) - vb[k] * f(va[k])) / (f(vb[k]) - f(va[k])))
        else:
            va.append(x[k-1])
            vb.append(vb[k-1])
            x.append((va[k]*f(vb[k]) - vb[k] * f(va[k])) / (f(vb[k]) - f(va[k])))

    return {'x': x[k], 'nr_it': k}
                      

    
puncte1 = []
puncte2 = []

st = -2
fin = 0
pt1 = Secanta(functie, st, fin, 0.000001)
pt2 = PozitieFalsa(functie, st, fin, 0.000001)
puncte1.append(pt1)
puncte2.append(pt2)

st = 0
fin = 1.4
pt1 = Secanta(functie, st, fin, 0.000001)
pt2 = PozitieFalsa(functie, st, fin, 0.000001)
puncte1.append(pt1)
puncte2.append(pt2)

st = 1.4
fin = 3
pt1 = Secanta(functie, st, fin, 0.000001)
pt2 = PozitieFalsa(functie, st, fin, 0.000001)
puncte1.append(pt1)
puncte2.append(pt2)

print("Metoda Secantei:")
print(puncte1)

print("Metoda Pozitiei False:")
print(puncte2)

desen_puncte = []
for i in range(len(puncte1)):
    desen_puncte.append(puncte1[i]['x'])


fig = plt.figure(1)
ax = plt.axes()
x = np.linspace(-2, 3, 200)
y = np.vectorize(functie)(x)
ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = f(x)')
ax.scatter(desen_puncte, np.zeros(3), color="g")
ax.grid(True, color = 'c')
plt.xticks(np.arange(-2,3,0.5))
plt.yticks(np.arange(-5, 5, 1))
ax.legend(loc='best')
plt.title('f(x) = y')
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
plt.show()