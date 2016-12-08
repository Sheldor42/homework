
def function(x):
    Savings=0.0
    for i in range(0,240):
        Savings=Savings*(1.06**(1/12))+x
    for n in range(0,360):
        Savings=Savings*1.06**(1/12)-1000

    return Savings
mini=0.0
maxi=1000000
for i in range(0,100000):
    a=function((mini+maxi)/2)
    if a<0:
        mini=((mini+maxi)/2)
    else:
        maxi=((mini+maxi)/2)
print("One has to save up {}€ every month".format((mini+maxi)/2))
