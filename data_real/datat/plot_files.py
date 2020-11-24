import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xa=np.loadtxt("Arduinovalues.txt",delimiter=',',skiprows=1)[:,0]
gsr= np.loadtxt("Arduinovalues.txt",delimiter=',',skiprows=1)[:,1]
temp=np.loadtxt("Arduinovalues.txt",delimiter=',',skiprows=1)[:,2]

xh = np.loadtxt("values.txt",delimiter=',',skiprows=1)[:,0]
hr = np.loadtxt("values.txt",delimiter=',',skiprows=1)[:,1]
rr = np.loadtxt("values.txt",delimiter=',',skiprows=1)[:,2]

xe = np.loadtxt("ECGvalues.txt",delimiter=',',skiprows=1)[:,0]
ecg = np.loadtxt("ECGvalues.txt",delimiter=',',skiprows=1)[:,1]

f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5)
ax1.plot(xa, gsr)
ax1.set_title('GSR')

ax2.plot(xa, temp)
ax2.set_title('Temperatur')

ax3.plot(xh,hr)
ax3.set_title('Heart rate')

ax4.plot(xh, rr)
ax4.set_title('RR')

ax5.plot(xe,ecg)
ax5.set_title('ECG')

plt.show()

