# possible solution:

import numpy as np
from scipy.optimize import brent
import matplotlib.pyplot as plt


F = 1000
c = .1
N = 30

@np.vectorize
def func(r):
    C = c * F * np.ones(N)
    C[-1] += F
    ii = np.arange(1, len(C)+1)
    return np.dot(C, (1+r)**(-ii)) * (1+r)**10

if __name__ == '__main__':
    min_p = brent(func)*100
    print(min_p)

    x = np.linspace(0.01, 0.2, 40)

    plt.figure()
    plt.plot(x*100, func(x))
    plt.show()
