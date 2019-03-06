import numpy as numpy
import matplotlib.pyplot as plt 

def main():
    D = 4
    s = 4
    mu1 = np.array([0, 0])
    mu2 = np.array([s, s])
    mu3 = np.array([0, s])

    N = 900
    X = np.zeros((N, D))
    X[:300, :] = np.random.randn(300, D) + mu1
    X[300:600, :] = np.random.randn(300, D) + mu2
    X[600: :] = np.random.randn(300, D) + mu3

    plt.scatter(X[:,0],X[:,1])
    plt.show()

    K = 3
    plot_k_means(X, K)

    K = 5
    plot_k_means(X, K)

if __name__ == '__main__':
    main()