import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage.restoration import denoise_wavelet
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
import pandas as pd
import os
import statistics


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

def baseLineRemoval(clipId,participant):
    pulsefile = np.loadtxt("data_real/P"+participant+"/data"+clipId+"/values.txt",delimiter=',',skiprows=1)
    arduinofile = np.loadtxt("data_real/P"+participant+"/data"+clipId+"/Arduinovalues.txt",delimiter=',',skiprows=1)
    pulse_base = np.loadtxt("data_real/P"+participant+"/dataFB/values.txt",delimiter=',',skiprows=1)
    arduino_base = np.loadtxt("data_real/P"+participant+"/dataFB/Arduinovalues.txt",delimiter=',',skiprows=1)
    base_rr_nonan = interpolateNaN(pulse_base[:,2])

    base_gsr=statistics.mean(arduino_base[:,1])
    base_temp=statistics.mean(arduino_base[:,2])
    base_hr=statistics.mean(pulse_base[:,1])
    base_rr=statistics.mean(base_rr_nonan)

    y_gsr = arduinofile[:,1]
    y_temp = arduinofile[:,2]

    y_rr = pulsefile[:,2]
    y_hr = pulsefile[:,1]

    yrr_nonan = interpolateNaN(y_rr)

    return y_gsr-base_gsr, y_temp-base_temp, y_hr-base_hr, yrr_nonan-base_rr


def preprosess(clipid,participant):

    yGSRport, ytemp, yhr, yrr = baseLineRemoval(clipid,participant)

    print(len(yGSRport))

    ecg= np.loadtxt("data_real/P"+participant+"/data"+clipid+"/ECGvalues.txt",delimiter=',',skiprows=1)
    xecg=ecg[:,0]
    yecg=ecg[:,1]

    start_time=xecg[0]

    df_ecg = pd.DataFrame(data=yecg,index=xecg,columns=["ecg"])

    xgsr=np.loadtxt("data_real/P"+participant+"/data"+clipid+"/Arduinovalues.txt",delimiter=',',skiprows=1)[:,0]

    gsr_startindex=0
    for i in xgsr:
        if i>start_time:
            break
        gsr_startindex+=1

    ygsr=PortValToResistance(yGSRport[gsr_startindex:])
    fygsr=savgol_filter(ygsr,3,2)

    arduinodata=np.column_stack((fygsr,ytemp[gsr_startindex:]))
    df_ard=pd.DataFrame(data=arduinodata,index=xgsr[gsr_startindex:],columns=["gsr","temp"])


    xhr = np.loadtxt("data_real/P"+participant+"/data"+clipid+"/values.txt",delimiter=',',skiprows=1)[:,0]
    hrv_startindex=0

    for j in xhr:
        if j>start_time:
            break
        hrv_startindex+=1



    hrvdata = np.column_stack((yhr[hrv_startindex:],yrr[hrv_startindex:]))
    df_hrv = pd.DataFrame(data=hrvdata,index=xhr[hrv_startindex:],columns=["hr","rr"])



    df_ecg.to_csv("data_real/P"+participant+"/data"+clipid+'/ecg_preprocessed.csv')
    df_ard.to_csv("data_real/P"+participant+"/data"+clipid+'/ard_preprocessed.csv')
    df_hrv.to_csv("data_real/P"+participant+"/data"+clipid+'/hrv_preprocessed.csv')



participants=[8]
data_names=["FA","FF","FS","FT"]

for p in participants:
    for d in data_names:
        preprosess(d,str(p))


