import numpy as np
import matplotlib.pyplot as plt

datafile=np.loadtxt("data/data199/Arduinovalues.txt",delimiter=',',skiprows=1)
x=datafile[:,0]
y=datafile[:,1]

ynew=[]

for i in y:
    ynew.append(((1024+2*i)*10000)/(512-i))

plt.plot(x,ynew)


plt.show()