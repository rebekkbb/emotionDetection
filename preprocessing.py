import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage.restoration import denoise_wavelet
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
import pandas as pd
import os


def interpolateNaN(y):
    ok = ~np.isnan(y)
    xp = ok.ravel().nonzero()[0]
    fp = y[~np.isnan(y)]
    x  = np.isnan(y).ravel().nonzero()[0]
    y[np.isnan(y)] = np.interp(x, xp, fp)
    return y

def PortValToResistance(gsrvals):
    f = lambda gsrvals : ((1024+2*gsrvals)*10000)/(512-gsrvals)
    return f(gsrvals)


def preprosess(clipid):

    xecg= np.loadtxt("data_real/data"+clipid+"/ECGvalues.txt",delimiter=',',skiprows=1)[:,0]
    yecg= np.loadtxt("data_real/data"+clipid+"/ECGvalues.txt",delimiter=',',skiprows=1)[:,1]

    start_time=xecg[0]

    df_ecg = pd.DataFrame(data=yecg,index=xecg,columns=["ecg"])


    xgsr=np.loadtxt("data_real/data"+clipid+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,0]
    yGSRport=np.loadtxt("data_real/data"+clipid+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,1]
    gsr_startindex=0
    for i in xgsr:
        if i>start_time:
            break
        gsr_startindex+=1

    ygsr=PortValToResistance(yGSRport[gsr_startindex:])
    fygsr=savgol_filter(ygsr,101,2)

    ytemp=np.loadtxt("data_real/data"+clipid+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,2][gsr_startindex:]

    arduinodata=np.column_stack((fygsr,ytemp))
    df_ard=pd.DataFrame(data=arduinodata,index=xgsr[gsr_startindex:],columns=["gsr","temp"])


    xhr = np.loadtxt("data_real/data"+clipid+"/values.txt",delimiter=',',skiprows=1)[:,0]
    yhr = np.loadtxt("data_real/data"+clipid+"/values.txt",delimiter=',',skiprows=1)[:,1]
    hrv_startindex=0

    for j in xhr:
        if j>start_time:
            break
        hrv_startindex+=1

    yrr = np.loadtxt("data_real/data"+clipid+"/values.txt",delimiter=',',skiprows=1)[:,2]
    yrr_nonan = interpolateNaN(yrr)

    hrvdata = np.column_stack((yhr[hrv_startindex:],yrr_nonan[hrv_startindex:]))
    df_hrv = pd.DataFrame(data=hrvdata,index=xhr[hrv_startindex:],columns=["hr","rr"])



    df_ecg.to_csv("data_real/data"+clipid+'/ecg_preprocessed.csv')
    df_ard.to_csv("data_real/data"+clipid+'/ard_preprocessed.csv')
    df_hrv.to_csv("data_real/data"+clipid+'/hrv_preprocessed.csv')


preprosess('b4')


