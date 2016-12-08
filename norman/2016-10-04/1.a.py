from math import exp,floor,ceil
import numpy as np
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



    print(valueTree[0][0])
    return(valueTree)

# Output the option price
#    oPrice = valueTree(1);
n=20    #never put above 200
T=0.01*n
r=0.05
K=1
S0=0.9
V=0.3
u=exp(V*((T/n)**(0.5)))
d=1/u
valueTree=binPriceCRR(K,S0,u,d,r,n,T,'call')
#calculates the price tree correctly
#this function gives me the value tree already imshow:
xDim=len(valueTree)
yDim=2*len(valueTree)-1
center=int(ceil(yDim/2))
Plot=np.ndarray(shape=(yDim,xDim))
Plot[0:yDim,0:xDim]=-1
for x in range(xDim):
    for y in range(len(valueTree[x])):
        Plot[center-len(valueTree[x])+2*y,x]=valueTree[x][y]
Green=copy(Plot)
Blue=copy(Plot)
Red=copy(Plot)
for x in range(xDim):
    for y in range(yDim):
        if Blue[y,x]<0:
            Blue[y,x]=0
            Green[y,x]=0
            Red[y,x]=0
        else:
            Blue[y,x]=1
            Green[y,x]=1
            Red[y,x]=1-Red[y,x]/max(valueTree[len(valueTree)-1])

print(Red)
Color=np.stack((Green.transpose(),Red.transpose(),Blue.transpose()))
print(Color)
print(Color.transpose().shape)
#print(Red)
#print(Plot)
#print(Blue)
#print(Plot)
#print(Plot.shape)
#B=plt.imshow([[[1.2,1.2,1.2]]])
A=plt.imshow(Color.transpose(), interpolation='nearest')
plt.show(A)
#Plot[y,x,0]: Red Value
#flag uselesss values as -1
