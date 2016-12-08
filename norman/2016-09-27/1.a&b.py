from math import exp
import numpy as np
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



    print(valueTree[0][0])

# Output the option price
#    oPrice = valueTree(1);
n=200    #never put above 200
T=0.005*n
r=0.05
K=1
S0=0.9
V=0.3
u=exp(V*((T/n)**(0.5)))
d=1/u
binPriceCRR(K,S0,u,d,r,n,T,'call')
#calculates the price tree correctly
