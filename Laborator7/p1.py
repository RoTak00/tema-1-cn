import sympy
import numpy
import matplotlib.pyplot as plt

# Problema 1. Sa se construiasca procedura DifFinCentr(f, x), care
# determina aproximativ derivata

def DifFinCentr(f, x):
    h = x[1] - x[0]

    df = (f(x + h) - f(x - h)) / (2 * h)

    return df

f = numpy.vectorize(lambda x : 1/ (1 + 25 * x * x))

# Problema 2. Fiind data functia f(x) = 1 / (1 + 25x^2) si intervalul (-1, 1), 
# sa se construiasca graficul derivatei f'(x) calculate numeric

if __name__ == "__main__":
    x = numpy.linspace(-1, 1, 500)

    fig, ax = plt.subplots(2)

    ax[0].plot(x, DifFinCentr(f, x), label="df(x) numeric", lw = 2, color = 'b', linestyle='-')
    ax[0].legend("best")
    ax[0].grid(True, color = 'c')
    

# Problema 3. Intr-o alta figura, sa se reprezinte eroarea absoluta

    # determine df
    a = sympy.Symbol("a")
    df_exp = sympy.diff((1 / (1 + 25 * a * a)), a)
    df_func = sympy.lambdify((a), df_exp, "numpy")
    
    df = df_func(x)
    ax[0].plot(x, df, lw = 2, color = "r", linestyle="--", label = "df(x) analitic")
    
    ax[1].plot(x, numpy.abs(df - DifFinCentr(f, x)), lw = 2, color = "g", linestyle="-", label = "eroare")
    ax[1].legend("best")
    ax[1].grid(True, color = 'c')
    plt.show()