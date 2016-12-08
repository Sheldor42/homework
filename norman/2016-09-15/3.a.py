import numpy
import matplotlib.pyplot as plot
####################################################################
YTM=numpy.arange(0,14).tolist()[::-1]
P1=0.06
P2=0.08
P3=0.1
####################################################################
def Value(YTM,p):
    Value=[1]
    for i in range(1,len(YTM)):
        Value.append(Value[i-1]*(1+p))
    return Value
####################################################################
V1=Value(YTM,P1)
V2=Value(YTM,P2)
V3=Value(YTM,P3)
####################################################################
plot.plot(YTM,V1,YTM,V2,YTM,V3)
plot.gca().invert_xaxis()
plot.xlabel("Years to maturity")
plot.ylabel("Current bond Value")
plot.show()
