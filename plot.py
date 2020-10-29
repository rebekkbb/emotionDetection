import numpy as np
import matplotlib.pyplot as plt

datafile=np.loadtxt("data/data199/values.txt",delimiter=',',skiprows=1)
x=datafile[:,0]
y=datafile[:,1]
y2=datafile[:,2]


"""for i in y:
    ynew.append(((1024+2*i)*10000)/(512-i))"""

plt.title("RR-intervals")
plt.xlabel("time stamp(sec from 1997)")
plt.ylabel("RR-interval(ms)")

plt.plot(x,y2)


plt.show()