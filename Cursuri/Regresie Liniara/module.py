import numpy as np
import matplotlib.pyplot as plt

def Regresie_Liniara(x, y):
    # Convert input lists to numpy arrays
    x = np.array(x)
    y = np.array(y)

    # Compute the required values for linear regression
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x**2)

    # Calculate the slope (m) and y-intercept (c) of the regression line
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    c = (sum_y - m * sum_x) / n

    plot_x = np.linspace(min(x), max(x), 100)
    plot_y = m * plot_x + c

    return plot_x, plot_y

def Regresie_Liniara_Gradient_Descent(x, y, learning_rate=0.01, num_iterations=1000):
    # Convert input lists to numpy arrays
    x = np.array(x)
    y = np.array(y)

    # Initialize slope (m) and y-intercept (c) with random values
    m = np.random.randn()
    c = np.random.randn()

    # Perform gradient descent
    for _ in range(num_iterations):
        # Predicted y values
        y_pred = m * x + c

        # Calculate gradients
        m_gradient = (2 / len(x)) * np.dot(x, (y_pred - y))
        c_gradient = (2 / len(x)) * np.sum(y_pred - y)

        # Update parameters
        m -= learning_rate * m_gradient
        c -= learning_rate * c_gradient

    # Return the slope and y-intercept as results of the linear regression
    plot_x = np.linspace(min(x), max(x), 100)
    plot_y = m * plot_x + c

    return plot_x, plot_y

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

    [plot_x, plot_y] = Regresie_Liniara(px, py)
    [plot_x2, plot_y2] = Regresie_Liniara_Gradient_Descent(px, py)

    fig = plt.figure(1)
    ax = plt.axes()



    ax.plot(plot_x, plot_y, linestyle='-', lw = 2, color = 'b', label = 'patrate')
    ax.plot(plot_x2, plot_y2, linestyle='-', lw = 2, color = 'g', label = 'rl')
    ax.scatter(px, py, color = 'r')

    ax.grid(True, color = 'c')


    ax.legend(loc='best')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('Graph of the points requested')

    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')

    plt.show()
