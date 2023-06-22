import numpy as np
import matplotlib.pyplot as plt

def SplineCubica(X, Y, derivata_fun_a, derivata_fun_b, vx):
    dim = len(X) - 1
    Mat = np.zeros((dim + 1, dim + 1))
    Mat[0][0] = 1
    Mat[dim][dim] = 1
    for i in range(1, dim):
        Mat[i][i] = 4
        Mat[i][i - 1] = 1
        Mat[i][i + 1] = 1
    
    H = np.zeros(dim)
    for i in range(dim):
        H[i] = X[i + 1] - X[i]
    
    W = np.zeros(dim + 1)
    W[0] = derivata_fun_a
    W[dim] = derivata_fun_b
    for i in range(1, dim):
        W[i] = (3 / H[i]) * (Y[i + 1] - Y[i - 1])
    B = np.linalg.solve(Mat, W)

    A = np.zeros(dim)
    C = np.zeros(dim)
    D = np.zeros(dim)

    for i in range(dim):
        A[i] = Y[i]
        C[i] = (3 / (H[i] * H[i])) * (Y[i + 1] - Y[i]) - (B[i + 1] + 2 * B[i]) / H[i]
        D[i] = (-2 / (H[i]**3)) * (Y[i + 1] - Y[i]) + (B[i + 1] + B[i]) / (H[i]**2)


    for j in range(dim):
        if (vx >= X[j]) and (vx <= X[j + 1]):
            S = A[j] + B[j] * (vx - X[j]) + C[j] * ((vx-X[j]) ** 2) + D[j] * ((vx-X[j])**3)

    return S


if __name__ == "__main__":
    X1 = np.array([1,   2,   5,   6,   7,   8,  10,  13,  17])
    Y1 = np.array([3, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5])
    dfa1 = 1
    dfb1 = -2/3

    X2 = np.array([17, 20,  23,  24,  25,  27, 27.7])
    Y2 = np.array([4.5, 7, 6.1, 5.6, 5.8, 5.2,  4.1])
    dfa2 = 3
    dfb2 = -4

    X3 = np.array([27.7, 28, 29, 30])
    Y3 = np.array([4.1, 4.3, 4.1, 3.0])
    dfa3 = 1/3
    dfb3 = -3/2

    graph_x1 = np.linspace(1, 17, 100)
    graph_x2 = np.linspace(17, 27.7, 100)
    graph_x3 = np.linspace(27.7, 30, 100)

    graph_y1 = np.array([SplineCubica(X1, Y1, dfa1, dfb1, x) for x in graph_x1])
    graph_y2 = np.array([SplineCubica(X2, Y2, dfa2, dfb2, x) for x in graph_x2])
    graph_y3 = np.array([SplineCubica(X3, Y3, dfa3, dfb3, x) for x in graph_x3])

    fig, ax = plt.subplots(1)

    ax.plot(graph_x1, graph_y1, color = 'b', label = "Slope1")
    ax.plot(graph_x2, graph_y2, color = 'b', label = "Slope2")
    ax.plot(graph_x3, graph_y3, color = 'b', label = "Slope3")

    ax.axis("equal")

    plt.show()
    