eroare_relativa = lambda prevx, x : abs((x - prevx) / x)

fun = lambda x : x**3 - 7*x**2 + 14 * x - 6
dfun = lambda x : 3*x**2 - 14*x+14
ddfun = lambda x: 6*x - 14

sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0

def Bisectie(f, a, b, eps = 10**-5):
    x_vechi = None

    while True:
        x = a + (b - a) / 2

        if x_vechi is not None and eroare_relativa(x_vechi, x) < eps:
            return x

        if sgn(f(a)) != sgn(f(x)):
            b = x
        else:
            a = x
        
        x_vechi = x


def Newton(f, df, ddf, x0, eps = 10**-5):
    x_vechi = x0

    if sgn(ddf(x0)) != sgn(f(x0)):
        print("Alege un alt x0")
        return None

    while True:
        x = x_vechi - f(x_vechi) / df(x_vechi)

        if eroare_relativa(x_vechi, x) < eps:
            return x

        x_vechi = x

def Secanta(f, x0, x1, a, b, eps = 10**-5):

    while True:
        x = (x0*f(x1) - x1*f(x0) ) / (f(x1) - f(x0))

        if not (a <= x <= b):
            print("alege alti 2 x initiali")
            return None

        if eroare_relativa(x1, x) < eps:
            return x

        x0 = x1
        x1 = x

def PozitieFalsa(f, a, b, eps=10**-5):
    x_vechi = None

    
    while True:
        x = a*f(b) - b*f(a) / (f(b) - f(a))

        if x_vechi is not None and eroare_relativa(x_vechi, x) < eps:
            return x

        if sgn(f(a)) != sgn(f(x)):
            b = x
        else:
            a = x

        x_vechi = x


if __name__ == "__main__":
    print(Bisectie(fun, 0, 1.4))
    print(Newton(fun, dfun, ddfun, 0.3))
    print(Secanta(fun, 0.3, 1.4, 0, 1.4))
    print(PozitieFalsa(fun, 0, 1.4))