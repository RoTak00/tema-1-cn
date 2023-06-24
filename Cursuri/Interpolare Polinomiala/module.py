import numpy as np
import matplotlib.pyplot as plt
import math

def reverse_poly(arr, x):
    res = 0
    for ind, val in enumerate(arr):
        res += (x ** ind) * val
    return res

def print_rev_poly(arr):
    for ind, val in enumerate(arr):
        if ind != 0:
            print(" + ", end="")
        print("%.3f" % val, end="")
        if ind != 0:
            print(f"x^{ind}", end="")
        print(" ", end="")

def Verificare(A, b, tol = 10 ** -16):
    """
    Verifies if the input matrix A and vector b are compatible for solving a linear system.
    
    :param A: a bidimensional matrix representing the system of linear equations
    :type A: numpy.ndarray
    
    :param b: a unidimensional vector representing the constants of the system
    :type b: numpy.ndarray
    
    :param tol: tolerance level for floating point comparisons, defaults to 10 ** -16
    :type tol: float
    
    :return: False if A or b are not compatible for solving a linear system, else None
    :rtype: bool or None
    """
    # Verificam ca A sa fie matrice bidimensionala
    if A.ndim != 2:
        print("Vectorul nu este bidimensional")
        return False

    # Verificam ca A sa fie matrice patratica
    if A.shape[0] != A.shape[1]:
        print("Matricea nu este patratica")
        return False    

    n = A.shape[0] # dimensiunea sistemului

    # Verificam ca b sa fie unidimensional 
    if b.ndim != 1:
        print("Vectorul b nu este unidimensional")
        return False
    # Verificam ca b sa aiba dimensiunea corecta
    if len(b) != n:
        print("Vectorul b nu are dimensiunea corecta")
        return False
    
    return True

def SubsAsc(A, b, tol = 10 ** -16):
    """
    This function solves a linear system of equations using the substitution method. 
    It takes a matrix A, a vector b, and an optional tolerance parameter tol. 
    If the matrix A is not lower triangular or the system is not compatible, the function returns None. 
    Otherwise, it calculates and returns the solution of the system as a vector of size n.
    """
    if Verificare(A, b, tol) == False:
        return None

    n = A.shape[0]

    # Verificam ca A sa fie inferior triunghiulara
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j]) > tol:
                print("Matricea nu e inferior triunghiulara")
                return None

    # Verificam ca sistemul sa fie compatibil determinat
    for i in range(n):
        if abs(A[i][i]) < tol:
                print("Sistemul nu e determinat")
                return None         

    # Calculam rezultatul sistemului
    res = np.zeros(n)
    for k in range(n):
        t = b[k]
        for j in range(k):
            t -= A[k][j] * res[j]

        t /= A[k][k]
        res[k] = t
    return res

def calcNewtonInX(x, C, vx):
    """
    Calculates the value of a polynomial using Newton's divided difference method.

    :param x: A float representing the value to calculate the polynomial at.
    :param C: A list of floats representing the coefficients of the polynomial.
    :param vx: A list of floats representing the x values associated with the coefficients.
    :return: A float representing the value of the polynomial at x.
    """
    res = C[0]
    for i in range(1, len(C)):
        temp_prod = C[i]
        for j in range(i):
            temp_prod *= (x - vx[j])
        res += temp_prod

    return res



def InterpolareSistemLiniar(px, py, precision = 200, padding = 0.05):
    """
    Interpolates polynomially using the given `px` and `py` points.

    :param px: A list of x-values.
    :type px: List[float]
    :param py: A list of y-values.
    :type py: List[float]
    :param precision: The number of points to compute on the interpolated curve.
    :type precision: int
    :param padding: The amount of padding to add to the plot.
    :type padding: float
    :return: A tuple containing the x and y values for the interpolated curve.
    :rtype: Tuple[List[float], List[float]]
    """
    fdim = len(px)

    mat = np.zeros((fdim, fdim))

    for ind, pt in enumerate(px):
        for i in range(fdim):
            mat[ind][i] = pt ** i

    sol = np.linalg.solve(mat, py)

    plot_x = np.linspace(min(px) - padding, max(px) + padding, precision)
    plot_y = [reverse_poly(sol, x) for x in plot_x]

    print_rev_poly(sol)
    return plot_x, plot_y

def InterpolareNewton(px, py, precision = 200, padding = 0.05):
    """
    Calculates the Newton interpolation polynomial using the given data points (px, py) and returns the x and y values for a plot of the polynomial. 
    
    :param px: a list of floats representing the x values of the data points
    :type px: list[float]
    
    :param py: a list of floats representing the y values of the data points
    :type py: list[float]
    
    :param precision: an optional integer representing the number of points to plot, defaults to 200
    :type precision: int
    
    :param padding: an optional float representing the space to add on either side of the plot, defaults to 0.05
    :type padding: float
    
    :return: a tuple containing two numpy ndarrays representing the x and y values of the plot
    :rtype: tuple(numpy.ndarray, numpy.ndarray)
    """

    din = len(px)
    A = np.zeros((dim, dim))

    for i in range(dim):
        for j in range(0, i + 1):
            A[i][j] = 1

    for j in range(1, dim):
        for i in range(j, dim):
            A[i][j] = A[i][j-1] * (px[i]-px[j-1])

    C = SubsAsc(A, py)

    plot_x = np.linspace(min(px) - padding, max(px) + padding, precision)
    plot_y = [calcNewtonInX(x, C, px) for x in plot_x]
    return plot_x, plot_y
    

def Lagrange(x, px, py):
    """
    Calculates the value of the Lagrange interpolation polynomial at a given point.

    :param x: The point to evaluate the polynomial at.
    :type x: float
    :param px: The list of x-coordinates of the known points.
    :type px: List[float]
    :param py: The list of y-coordinates of the known points.
    :type py: List[float]
    :return: The value of the Lagrange interpolation polynomial at x.
    :rtype: float
    """
    result = 0

    for k in range(len(px)):
        product = py[k] 
        for j in range(len(px)):
            if j != k:
               product *= (x - px[j]) / (px[k] - px[j])
        result += product

    return result

def InterpolareLagrange(px, py, precision = 200, padding = 0.05):
    """
    Interpolates a set of points using Lagrange polynomial interpolation.
    
    Args:
    - px: a list or array of x-coordinates for the points to be interpolated
    - py: a list or array of y-coordinates for the points to be interpolated
    - precision: an optional integer representing the number of points to plot between the minimum and maximum x-values (default 200)
    - padding: an optional float representing the padding to add to the minimum and maximum x-values for plotting purposes (default 0.05)
    
    Returns:
    - plot_x: a 1D array of x-values for the interpolated points
    - plot_y: a 1D array of y-values for the interpolated points
    """
    plot_x = np.linspace(min(px) - padding, max(px) + padding, precision)

    plot_y = [Lagrange(x, px, py) for x in plot_x]

    return plot_x, plot_y

def DDHelper(arr, px, x):
    res = 0

    for i in range(len(arr)):
        subres = arr[i]
        for j in range(i):
            subres *= (x - px[j])
        res += subres

    return res
def InterpolareDiferenteDivizate(px, py, precision = 200, padding = 0.05):
    k = len(px)

    dd = np.zeros((k, k))

    for i in range(k):
        dd[i, 0] = py[i]

    for j in range(1, k):
        for i in range(j, k):
            dd[i, j] = (dd[i, j - 1] - dd[i - 1, j - 1]) / (px[i] - px[i - j])

    Q = np.zeros(k)
    for i in range(k):
        Q[i] = dd[i,i]

    plot_x = np.linspace(min(px) - padding, max(px) + padding, precision)
    plot_y = [DDHelper(Q, px, x) for x in plot_x]

    return plot_x, plot_y


def functie(x):
    return math.sin(x)

if __name__ == "__main__":
    q = int(input("Puncte sau functie? 1 / 2\n"))
    pts = []

    if q == 1:
        x = int(input("How many points do you want to plot? "))
        pts = [[0, 0] for i in range(x)]
        for i in range(x):
            pt = [float(x) for x in input("Next point: ").split()]
            if len(pt) != 2:
                exit()
            pts[i] = pt
    elif q == 2:
        a, b = [float(x) for x in input("Cele 2 capete\n").split()]
        n = int(input("Cate diviziuni?\n"))

        q2 = int(input("Tip diviziuni? (1 - normal / 2 - chebyshev)"))
        px = []

        if q2 == 1:
            px = np.linspace(a, b, n + 1)
        elif q2 == 2:
            px = np.array([(a + b) / 2 + ((b - a) / 2) * math.cos((n + i) * math.pi / n) for i in range(n + 1)])

        pts = [(x, functie(x)) for x in px]
    else:
        print("Nu ai introdus corect.")
        exit(1)
        
    pts = np.array(pts)
    dim = len(pts)

    px = np.array([x[0] for x in pts])
    py = np.array([x[1] for x in pts])

    #[plot_x, plot_y] = InterpolareSistemLiniar(px, py, 500)
    #[plot_x, plot_y] = InterpolareNewton(px, py, 500)
    #[plot_x, plot_y] = InterpolareLagrange(px, py, 500)
    [plot_x, plot_y] = InterpolareDiferenteDivizate(px, py, 500)

    fig = plt.figure(1)
    ax = plt.axes()



    ax.plot(plot_x, plot_y, linestyle='-', lw = 2, color = 'b', label = 'fun')
    ax.scatter(px, py, color = 'r')

    ax.grid(True, color = 'c')


    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Graph of the points requested')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')

    plt.show()


