# a possible solution:

from pylab import *
from scipy.optimize import brentq


PV = 0.75
F = 1
c = 0.10
n = 10
m = 2
C = array(n*m*[(c*F)/m])
ii = arange(1,n*m+1)

def ytm(r):
    return dot(C, (1+(r/m))**(-ii)) + (F/(1+(r/m))**(n*m)) - PV

print(brentq(ytm,-0.1,1.1))
