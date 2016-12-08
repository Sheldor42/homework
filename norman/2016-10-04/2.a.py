from math import exp,floor,ceil,log
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from copy import copy
def binPriceCRR(X,S0,u,d,r,n,T,type):
# Calculate the Cox Ross Rubinstein model parameters
    T=T/n
    a = exp(r*(T));
    p = (a-d)/(u-d);
    priceTree=[]
    priceTree.append([S0])
    for i in range(n):
        dim=len(priceTree[i])
        ll=[]
        for a in range(dim):
            ll.append(priceTree[i][a]*u)
        ll.append(priceTree[i][dim-1]*d)
        priceTree.append(ll)
    #print('last entry price tree',priceTree[n])
        # Calculate the value at expiry
    valueTree=[]
    if type=='call':
        valueTree.append(list(-X*np.ones(len(priceTree[len(priceTree)-1]))+priceTree[len(priceTree)-1]))
    elif type=='put':
        valueTree.append(list(X*np.ones(len(priceTree[len(priceTree)-1]))-priceTree[len(priceTree)-1]))


    #print('Value tree',valueTree)

    def neatfunction():
        #thing can't fall below zero

        for i in range(len(valueTree)):
            for x in range(len(valueTree[i])):
                if valueTree[i][x]<0:
                    valueTree[i][x]=0


    def previousStep():
        Current=valueTree[0]
        New=[]
        for x in range(len(Current)-1):
            New.append(exp(-r*(T))*(p*Current[x]+(1-p)*Current[x+1]))
        return [New]+valueTree
    neatfunction()



    for i in range(len(valueTree[0])-1):
        valueTree=previousStep()



    return valueTree[0][0]

# Output the option price
#    oPrice = valueTree(1);
n=2000    #never put above 200
T=10
r=0.05
K=1
S0=0.9
V=0.3
u=exp(V*((T/n)**(0.5)))
d=1/u
#binom=binPriceCRR(K,S0,u,d,r,n,T,'call')

x=log(S0/K)+(r+(V**2)/2)*T/(V*(T**(0.5)))
C=S0*norm.cdf(x)-K*exp(-r*T)*norm.cdf(x-V*(T**(0.5)))
Error=[]
Counter=[]
#values should not be negative otherwise log can't work
a=1
i=a+1
while i in range(a,501):
    z=C-binPriceCRR(K,S0,u,d,r,i,T,'call')
    if z<=0:
        i=a+2
        a+=1
        Error=[]
        Counter=[]
    else:
        Error.append(log(z))
        Counter.append(i)
        i+=1
plt.plot(Counter,Error)
plt.show()
plt.xlabel('Steps')
plt.ylabel('ln(Error )')



print(Error)









#
