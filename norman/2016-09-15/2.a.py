import numpy
import matplotlib.pyplot as plot
####################################################################
YTM=numpy.arange(0,101)
P1=0.02
P2=0.06
P3=0.12
Yield=0.06
V=1000
####################################################################
def Price(P,V,YTM,Yield):
    return YTM*(1+P)*V/Yield
####################################################################
def Vol(YTM,P1,P2,P3):
    Price1=Price(P1,V,YTM,Yield)
    Price2=Price(P2,V,YTM,Yield)
    Price3=Price(P3,V,YTM,Yield)
    dev=[]
    for i in range(0,101):
        dev.append(numpy.std([Price1[i],Price2[i],Price3[i]]))
    return dev
####################################################################
dev=Vol(YTM,P1,P2,P3)
#print(len(dev))
#print(len(YTM))
####################################################################
plot.plot(YTM,dev)
plot.xlabel("Years to maturity")
plot.ylabel("Standard deviation")
plot.show()
