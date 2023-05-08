import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math

def eroare(x1, x2):
    return abs((x2 - x1) / x2)

def functie(x):
    return x*x*x - 7 * x * x + 14 * x - 6

def radacina(func, a, b, tabel, e = 0.001):
    cnt = 0
    x_vechi = -1
    
    while True:
        x = (a+b) / 2

        y = func(x)
        er = ""
        if cnt != 0:
            er = eroare(x_vechi, x)
        logaritm = (float)((b - a) / (2 ** (cnt)))

        tabel.add_row([cnt + 1, x, y, e, logaritm])

        if cnt != 0 and er < e:
            return {'x':x, 'it':cnt}

        if func(a) * func(x) < 0:
            b = x
        else:
            a = x
        
        cnt += 1
        x_vechi = x
    

puncte = []
tabele = []

st = 0
fin = 1
tabel = PrettyTable(['k', 'x_k', 'f(x_k)', 'rel err', '(b-a)/2^(k-1)'])
pt = radacina(functie, st, fin, tabel, 10**-6)
puncte.append(pt['x'])
tabele.append(tabel)

st = 2.5
fin = 3.05
tabel = PrettyTable(['k', 'x_k', 'f(x_k)', 'rel err', '(b-a)/2^(k-1)'])
pt = radacina(functie, st, fin, tabel, 10**-6)
puncte.append(pt['x'])
tabele.append(tabel)

st = 3.05
fin = 4
tabel = PrettyTable(['k', 'x_k', 'f(x_k)', 'rel err', '(b-a)/2^(k-1)'])
pt = radacina(functie, st, fin, tabel, 0.000001)
puncte.append(pt['x'])
tabele.append(tabel)


print("Radacini:")
print(puncte)

for i in range(3):
    print(f"x = {puncte[i]}:")
    print(tabele[i])

fig = plt.figure(1)
ax = plt.axes()
x = np.linspace(0, 4, 100)
y = functie(x)
ax.plot(x, y, linestyle='-', lw = 2, color = 'b', label = 'y = f(x)')
ax.scatter(puncte, np.zeros(3), color="g")
ax.grid(True, color = 'c')
plt.xticks(np.arange(0,4,0.5))
plt.yticks(np.arange(-10,10,2))
ax.legend(loc='best')
plt.title('f(x) = y')
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
plt.show()
