# exemplary solution:

import numpy as np
import matplotlib.pyplot as plt


n = 15
m = 2
N = m*n
F = 100
periods = np.arange(N+1)
years = periods[::-1]/m

@np.vectorize
def FV1(r, p):
    C = 0.08/m * F * np.ones(N)
    C[-1] += F

    ii = np.arange(1, len(C)+1)

    return np.dot(C, (1+r/m)**(-ii)) * (1+r/m)**p / \
           np.dot(C, (1+.08/m)**(-ii))

plt.figure()
plt.plot(years, FV1(0.06, periods),
         years, FV1(0.08, periods),
         years, FV1(0.10, periods))

plt.legend(('r = 6%',
            'r = 8%',
            'r = 10%'),
        loc = 'upper left')
plt.show()
