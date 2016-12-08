import numpy
N=int(input())
P=float(input())
C=100.0*numpy.arange(3,N+3);
C[0]=C[0]-P;
C=C[::-1];
B=numpy.roots(C)
for i in range(0,len(C)-1):
    if numpy.imag(B)[i]==0:
        Z=numpy.real(B)[i]

print(Z)
