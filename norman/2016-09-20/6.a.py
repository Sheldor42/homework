#please don't change the layout of the .csv file issued by ECB
import numpy
import csv
import os
import matplotlib.pyplot as plt
if os.path.exists('yc_latest.csv')==True:
    Path='yc_latest.csv'
else:
    Path=input("Sadly the file yc_latest is not in your WD please enter the path of the file you'd like to evaluate: \n")
with open(Path,'r') as f:
    reader=csv.reader(f)
    String=list(reader)
VD=[]
for i in String:
    for s in i:
        if 'Yield curve spot rate' in s and 'triple A' not in s:
            VD.append(i)
VD2=[]
for i in range(0,len(VD)):
    VD2.append(float(VD[i][1]))
plt.plot(numpy.arange(0,len(VD)),VD2)
plt.title('ECB yield values using the spot rate')
plt.xlabel('Month')
plt.ylabel('Yield')
plt.show()
