import numpy
N=float(input("Number of Periods: "))
y=float(input("Period interest rate: "))
def Presesent_Value_arrays(N,y,C):
    A=numpy.arange(0,N);
    B=1/((1+y)**A);
    D=sum(C*B);
    return D
A=Presesent_Value_arrays(N,y,100.0*numpy.arange(3,N+3))
#a=A[N-1];
print("Your present value is {:>20}".format(A))
#[Finished in 0.21s]
#slowest method indecates lowest efficency
