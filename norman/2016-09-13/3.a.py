# a possible solution:

import numpy as np
import matplotlib.pyplot as plt


n = 10
m = 2
r = .06
F = 1000

periods = np.arange(n*m+1)
years = periods / m

def func(c):
    s = r / m
    C = c * F / m
    return C*(1-(1+s)**(-periods))/s + F*(1+s)**(-periods)

plt.figure()
for c in (.02, .06, .12):
    plt.plot(years, func(c), label='{}%'.format(c*100))
plt.legend(loc='best')
plt.show()
