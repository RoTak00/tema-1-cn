import numpy as np
import matplotlib.pyplot as plt
import math


def InterpolareLiniaraHelper(x, px, A, B):
    for j in range(len(A)):
        if x >= px[j] and x <= px[j + 1]:
            return A[j] + B[j] * (x - px[j])
    
    return 0
    
def InterpolareLiniara(px, py, precision = 500):
    """
    This function calculates the linear interpolation of a set of points given their 
    x and y coordinates, and returns the interpolated values for a given number of 
    points (default: 500) within the range of the input x values. 

    :param px: A list of x-coordinates of the input points.
    :type px: list

    :param py: A list of y-coordinates of the input points.
    :type py: list

    :param precision: The number of interpolated points to generate. Default is 500.
    :type precision: int

    :return: A tuple containing the x and y coordinates of the interpolated points.
    :rtype: tuple
    """
    nr_partitii = len(px) - 1

    A = [py[i] for i in range(nr_partitii)]
    B = [(py[i+1] - py[i]) / (px[i+1]-px[i]) for i in range(nr_partitii)]

    plot_x = np.linspace(min(px), max(px), precision)
    plot_y = [InterpolareLiniaraHelper(x, px, A, B) for x in plot_x]

    return plot_x, plot_y

def InterpolarePatraticaHelper(x, px, A, B, C):
    for j in range(len(A)):
        if x >= px[j] and x <= px[j + 1]:
            return A[j] + B[j] * (x - px[j]) + C[j] * (x - px[j]) ** 2
    
    return 0

def InterpolarePatratica(px, py, precision = 500):
    nr_partitii = len(px) - 1

    pts = [[px[i], py[i]] for i in range(len(px))]
    pts.sort(key = lambda x: x[0])

    px = [pt[0] for pt in pts]
    py = [pt[1] for pt in pts]
    
    h = [px[i + 1] - px[i] for i in range(nr_partitii)]
    A = [py[i] for i in range(nr_partitii)]
    B = np.zeros(nr_partitii + 1)
    for j in range(nr_partitii - 1, -1, -1):
        B[j] = (2.0 / h[j]) * (py[j + 1] - py[j]) - B[j + 1]
    C = [(1 / h[j]**2) * (py[j + 1] - py[j] - h[j] * B[j]) for j in range(nr_partitii)]

    plot_x = np.linspace(min(px), max(px), precision)
    plot_y = [InterpolarePatraticaHelper(x, px, A, B, C) for x in plot_x]

    return plot_x, plot_y

def InterpolareCubicaHelper(x, px, A, B, C, D):
    for j in range(len(A)):
        if x >= px[j] and x <= px[j + 1]:
            return A[j] + B[j] * (x - px[j]) + C[j] * (x - px[j]) ** 2 + D[j] * (x - px[j]) ** 3
    
    return 0

def InterpolareCubica(px, py, precision = 500):
    """
    Interpolates a set of points using the Cubic Interpolation method.
    
    Args:
    - `px` list of floats: The x-coordinates of the points to interpolate.
    - `py` list of floats: The y-coordinates of the points to interpolate.
    - `precision` int: The number of points to use for the interpolated function.

    Returns:
    - `plot_x` ndarray: The interpolated x-coordinates.
    - `plot_y` ndarray: The interpolated y-coordinates.
    """
    pts = [[px[i], py[i]] for i in range(len(px))]
    pts.sort(key = lambda x: x[0])

    px = [pt[0] for pt in pts]
    py = [pt[1] for pt in pts]

    dim = len(px) - 1
    Mat = np.zeros((dim + 1, dim + 1))
    Mat[0][0] = 1
    Mat[dim][dim] = 1
    for i in range(1, dim):
        Mat[i][i] = 4
        Mat[i][i - 1] = 1
        Mat[i][i + 1] = 1
    
    H = np.zeros(dim)
    for i in range(dim):
        H[i] = px[i + 1] - px[i]
    
    W = np.zeros(dim + 1)
    W[0] = 0
    W[dim] = 0
    for i in range(1, dim):
        W[i] = (3 / H[i]) * (py[i + 1] - py[i - 1])
    B = np.linalg.solve(Mat, W)

    A = np.zeros(dim)
    C = np.zeros(dim)
    D = np.zeros(dim)

    for i in range(dim):
        A[i] = py[i]
        C[i] = (3 / (H[i] * H[i])) * (py[i + 1] - py[i]) - (B[i + 1] + 2 * B[i]) / H[i]
        D[i] = (-2 / (H[i]**3)) * (py[i + 1] - py[i]) + (B[i + 1] + B[i]) / (H[i]**2)

    plot_x = np.linspace(min(px), max(px), precision)
    plot_y = [InterpolareCubicaHelper(x, px, A, B, C, D) for x in plot_x]


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

    #[plot_x, plot_y] = InterpolareLiniara(px, py)
    #[plot_x, plot_y] = InterpolarePatratica(px, py)
    [plot_x, plot_y] = InterpolareCubica(px, py)

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


