from timeit import default_timer as timer
import numpy;
import scipy.optimize as sci;
Test_case=False;


N=input("N (leave empty to run test case): ")
if N:
    P=float(input("P: "))
    N=int(N)
else:
    Test_case=True;

#------------------------------------------------------

def Newton(N,P,Case):
    C=100.0*numpy.arange(3,N+3);
    C[0]=C[0]-P;
#    C=C[::-1]
    f="{}".format(C[0])
    df="0"
    for i in range(1,len(C)):
        f=f+"+({})*((1+x)**({}))".format(C[i],-i)
    for i in range(1,len(C)):
        df=df+"+({})*({})*((1+x)**({}))".format(C[i],-i,-i-1)
#    print(f)
#    print(df)
    func= lambda x: eval(f)
    dfunc= lambda x: eval(df)
    if Case==0:
        Start=timer()
        sci.newton(func,0)
        return timer()-Start
    if Case==1:
        Start=timer()
        sci.newton(func,0,dfunc)
        return timer()-Start
    if Case==2:
        Start=timer()
        sci.brentq(func,0,1)
        return timer()-Start

#-------------------------------------------------------
if Test_case==False:
    print("For the secant method we have {}s.".format(Newton(N,P,0)))
    print("For the newton method we have {}s.".format(Newton(N,P,1)))
    print("For brent's method we have {}s.".format(Newton(N,P,2)))
if Test_case==True:
    N=20;P=20000;
    print("For the secant method we have {}s.".format(Newton(N,P,0)))
    print("For the newton method we have {}s.".format(Newton(N,P,1)))
    print("For brent's method we have {}s.".format(Newton(N,P,2)))
    N=200;P=1500000
    print("For the secant method we have {}s.".format(Newton(N,P,0)))
    print("For the newton method we have {}s.".format(Newton(N,P,1)))
    print("For brent's method we have {}s.".format(Newton(N,P,2)))
