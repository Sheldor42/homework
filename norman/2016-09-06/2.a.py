import numpy
import pandas
r=float(input("effective annual interest rate: "))
P=float(input("loan: "))
m=float(input("compounding periods: "))
n=float(input("term of mortage in years: "))
r=r/m
payment=r*P/(1-((1+r)**-(n*m)))
effective=(1+r)**(m)-1
principle=[]
interest=[]
remainder=[P]
for i in range(0,int(n*m)):
    interest.append(remainder[i]*r)
    principle.append(payment-interest[i])
    remainder.append(remainder[i]-principle[i])

print("The payment is: {:>15}".format(payment))
print("The effective interest rate is {:>15}".format(effective))
#for i in range(0,int(n*m)):
    #print(interest[i])
    #print(principle[i])
    #print(remainder[i+1])
#    n=i+1
#    print("in month '{}' the interest part is '{}', the principle part is '{}', '{}' is remainding.\n".format(n, interest[i], principle[i], remainder[i+1]))
del remainder[0]
#print(len(remainder),len(principle),len(interest),len(numpy.linspace(0,n*m,1)))
data={"Interest":interest,"Principle":principle,"Remainding":remainder}
print(pandas.DataFrame(data))
