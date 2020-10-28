import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage.restoration import denoise_wavelet
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
import pandas as pd
import os



cliplengths={'2':85,'3':195,'4':133,'5':245,'6':233,'7':259,'8':187,'9':271,'10':159,'11':104,'12':28,'13':281,'14':111,'15':269,'16':272,'17':252,'18':156,'19':199,'20':187,'21':150}

def interpolateNaN(y):
    ok = ~np.isnan(y)
    xp = ok.ravel().nonzero()[0]
    fp = y[~np.isnan(y)]
    x  = np.isnan(y).ravel().nonzero()[0]
    y[np.isnan(y)] = np.interp(x, xp, fp)
    return y

def preprosess(clipnum,participant):
    xgsr=np.loadtxt("data/"+participant+"/data"+clipnum+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,0]
    ygsr=np.loadtxt("data/"+participant+"/data"+clipnum+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,1]

    ytemp=np.loadtxt("data/"+participant+"/data"+clipnum+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,2]

    xhr = np.loadtxt("data/"+participant+"/data"+clipnum+"/values.txt",delimiter=',',skiprows=1)[:,0]
    yhr = np.loadtxt("data/"+participant+"/data"+clipnum+"/values.txt",delimiter=',',skiprows=1)[:,1]

    yrr = np.loadtxt("data/"+participant+"/data"+clipnum+"/values.txt",delimiter=',',skiprows=1)[:,2]

    xecg= np.loadtxt("data/"+participant+"/data"+clipnum+"/ECGvalues.txt",delimiter=',',skiprows=1)[:,0]
    yecg= np.loadtxt("data/"+participant+"/data"+clipnum+"/ECGvalues.txt",delimiter=',',skiprows=1)[:,1]

    yrr_nonan=interpolateNaN(yrr)

    ggsr= interp1d(xgsr, ygsr, kind='previous',fill_value="extrapolate")
    gtemp= interp1d(xgsr, ytemp, kind='previous',fill_value="extrapolate")
    ghr= interp1d(xhr, yhr, kind='previous',fill_value="extrapolate")
    grr= interp1d(xhr, yrr_nonan, kind='previous',fill_value="extrapolate")

    preprosGSR=savgol_filter(ggsr(xecg),101,2)
    alldata=np.column_stack((ghr(xecg),grr(xecg),yecg,preprosGSR,gtemp(xecg)))

    df=pd.DataFrame(data=alldata,index=xecg,columns=['hr','rr','ecg','gsr','temperature'])

    if (xecg[-1]-xecg[0])>cliplengths[clipnum]:
        cutteddf=df.loc[xecg[0]:xecg[0]+cliplengths[str(clipnum)]]
        cutteddf.to_csv("data/"+participant+"/data"+clipnum+'/preprocessedData.csv')
    else:
        df.to_csv("data/"+participant+"/data"+clipnum+'/preprocessedData.csv')
        print(clipnum)

for i in range(2,22):
    preprosess(str(i),'r')


