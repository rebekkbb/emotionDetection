import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""files=[1,4,6,7,11,12,13,14,18,19,20]
x=np.arange(0,33,1)

matr=[]
for i in files:
    ynew=[]
    datafile=np.loadtxt("data/data"+str(i)+"99/values.txt",delimiter=',',skiprows=1)
    y=datafile[:,1][:33]
    y2=datafile[:,2][:33]
    for i in y:
        ynew.append(((1024+2*i)*10000)/(512-i))
    matr.append(y)
meanlist=np.mean(matr,axis=0)

datafunny=np.loadtxt("data/data2/values (9).txt",delimiter=',',skiprows=1)
plt.plot(x,meanlist)
plt.plot(x,datafunny[:,1][57:])


plt.title("GSR")
plt.xlabel("time stamp(sec from 1997)")
plt.ylabel("GSR")



plt.show()"""



#datafile=pd.read_csv("data_real/dataf/")
data =pd.read_csv("data_real/datat/hrv_preprocessed.csv")
basedata = pd.read_csv("data_real/datab4/hrv_preprocessed.csv",)
baseecg = np.loadtxt("data_real/datab1/ECGvalues.txt",delimiter=',',skiprows=1)
tecg = np.loadtxt("data_real/datah/ECGvalues.txt",delimiter=',',skiprows=1)

#newarr=np.subtract(data[:,2],basedata[-len(data):,2])


"""y=datafile[:,1][:-6000]
y2=datafile[:,1][-6000:]
y3=datafunny[:,1][-6000:]

plt.psd(y,500,label='fear')
plt.psd(y2,500,label='calm')
plt.psd(y3,500,label='happy')
plt.legend()
plt.plot(np.arange(0,len(basedata[:,2]),1),basedata[:,2])
plt.plot(np.arange(0,len(data[:,2]),1),data[:,2])"""

plt.psd(data["rr"].to_numpy(),label='happy')
plt.psd(basedata["rr"].to_numpy(),label='base')
plt.legend()
plt.show()
