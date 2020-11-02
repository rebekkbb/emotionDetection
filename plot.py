import numpy as np
import matplotlib.pyplot as plt

files=[1,3,4,5,6,7]
x=np.arange(0,30,1)
for i in files:
    ynew=[]
    datafile=np.loadtxt("data/data"+str(i)+"99/Arduinovalues.txt",delimiter=',',skiprows=1)
    y=datafile[:,1][:30]
    y2=datafile[:,2][:30]
    for i in y:
        ynew.append(((1024+2*i)*10000)/(512-i))
    plt.plot(x,ynew)


plt.title("RR-intervals")
plt.xlabel("time stamp(sec from 1997)")
plt.ylabel("RR-interval(ms)")



plt.show()