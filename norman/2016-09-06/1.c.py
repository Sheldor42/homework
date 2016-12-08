import numpy
N=float(input("Number of Periods: "))
y=float(input("Period interest rate: "))
def Presesent_Value_arrays(N,y,C):
    Sum=0
    for i in range(0,int(N)):
        Sum+=C[i]*(1+y)**(-i)
    return Sum
A=Presesent_Value_arrays(N,y,100.0*numpy.arange(3,N+3))
#a=A[N-1];
print("Your present value is {:>20}".format(A))
#[Finished in 0.174s]
#fastet method inecates high efficency
