import numpy as np
import matplotlib.pyplot as plt

files=[1,4,6,7,11,12,13,14,18,19,20]
x=np.arange(0,33,1)

matr=[]
for i in files:
    ynew=[]
    datafile=np.loadtxt("data/data"+str(i)+"99/values.txt",delimiter=',',skiprows=1)
    y=datafile[:,1][:33]
    y2=datafile[:,2][:33]
    """for i in y:
        ynew.append(((1024+2*i)*10000)/(512-i))"""
    matr.append(y)
meanlist=np.mean(matr,axis=0)

datafunny=np.loadtxt("data/data2/values (9).txt",delimiter=',',skiprows=1)
plt.plot(x,meanlist)
plt.plot(x,datafunny[:,1][57:])


plt.title("GSR")
plt.xlabel("time stamp(sec from 1997)")
plt.ylabel("GSR")



plt.show()