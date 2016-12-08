import numpy
N=float(input("Number of Periods: "))
y=float(input("Period interest rate: "))
def Presesent_Value_arrays(N,y,C):
    C=C[::-1]
    x=1/(1+y);
    return numpy.polyval(C,x)

A=Presesent_Value_arrays(N,y,100.0*numpy.arange(3,N+3))
#a=A[N-1];
print("Your present value is {:>20}".format(A))
#[Finished in 0.179s]
#almost as fast as the simple loop indecates high efficency
