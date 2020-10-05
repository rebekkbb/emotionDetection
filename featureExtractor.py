import statistics
import numpy as np
from scipy.stats import linregress

def GSRfeatures(clipNum):
    datafile=np.loadtxt("data/data"+clipNum+"/GSR_denoised.txt",delimiter=',',skiprows=1)
    x=datafile[:,0]
    y=datafile[:,1]

    mean5sec= []
    std5sec= []
    slopes5sec= []
    intercept5sec= []
    r_value5sec= []
    p_value5sec= []
    maxval = max(y)
    minval = min(y)

    i_start=0
    i_end=0

    k=0
    j=0
    while k<=len(x)-5:
        if int(x[k])==int(x[i_start])+1:
            while j<len(x) and x[j]<x[k]+6:
                j+=1
            i_end = j
            i_start = k

            mean5sec.append(statistics.mean(y[i_start:i_end]))
            std5sec.append(statistics.stdev(y[i_start:i_end]))

            slope, intercept, r_value, p_value, std_err = linregress(x[i_start:i_end],y[i_start:i_end])
            slopes5sec.append(slope)

            j=i_start
        k+=1
    print(slopes5sec)
    print(statistics.stdev(y))

GSRfeatures('1')

  



