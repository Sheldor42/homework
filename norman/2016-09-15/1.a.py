import matplotlib.pyplot as plot

N=10
P=0.08
V=1000

def Yield(N,P,V,Price):
    return N*(1+P)*V/Price

A=[]
B=[]

for i in range(500,1500):
    A.append(i)
    B.append(Yield(N,P,V,i))

plot.plot(A,B)
plot.xlabel("Price in €")
plot.ylabel("Yield")
plot.show()
