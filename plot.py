import numpy as np
import matplotlib.pyplot as plt

datafile=np.loadtxt("data/data199/Arduinovalues.txt",delimiter=',',skiprows=1)
x=datafile[:,0]
y=datafile[:,1]
y2=datafile[:,2]



plt.plot(x,y2)


plt.show()