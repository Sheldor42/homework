# a possible solution:

import numpy as np
import matplotlib.pyplot as plt

F = 1000

n = 100
m = 2
N = m*n
periods = np.arange(N+1)
years = periods/m

def volatility(c, N):
    if N == 0: return 0.

    C = F * c/m * np.ones(N)
    C[-1] += F

    rp = .06/m
    ii = np.arange(1, len(C)+1)

    return -(np.dot(-C*ii, (1+rp)**(-ii-1)))/(np.dot(C, (1+rp)**(-ii)))
volatility = np.vectorize(volatility)

plt.figure()
plt.plot(
    years, volatility(.02, periods),
    years, volatility(.06, periods),
    years, volatility(.12, periods))
plt.legend((
        'c = 2%',
        'c = 6%',
        'c = 12%'
    ), loc='best')
plt.show()
