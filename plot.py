import numpy as np
import matplotlib.pyplot as plt

datafile=np.loadtxt("data/data6/values.txt",delimiter=',',skiprows=1)
x=datafile[:,0]
y=datafile[:,1]

plt.plot(x,y)


plt.show()