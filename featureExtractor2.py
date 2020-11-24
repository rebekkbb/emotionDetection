import statistics
import numpy as np
from scipy.stats import linregress, kurtosis, skew, sem
import pandas as pd
import math
import preprocessing
from scipy import signal
import matplotlib.pyplot as plt

def GSRfeatures(clipid):
    datafile=pd.read_csv('real_data/'+clipid+'/ard_preprocessed.csv',index_col=0)["gsr"]

    meanGSR = statistics.mean(datafile)
    stdGSR = statistics.stdev(datafile)
    slopeGSR, interceptGSR, r_valueGSR, p_valueGSR, std_errGSR = linregress(datafile.index,datafile)
    maxvalGSR = max(datafile)
    minvalGSR = min(datafile)
    modeGSR = statistics.mode(datafile)
    kurtosisGSR = kurtosis(datafile)
    skewnessGSR = skew(datafile)

    return meanGSR, stdGSR, slopeGSR, maxvalGSR, minvalGSR, modeGSR, kurtosisGSR, skewnessGSR

def Tempfeatures(clipid):
    datafile=pd.read_csv('real_data/'+clipid+'/ard_preprocessed.csv',index_col=0)["temp"]

    meanT=statistics.mean(datafile)
    stdT=statistics.stdev(datafile)
    minvalT=statistics.min(datafile)
    maxvalT=statistics.max(datafile)
    modeT=statistics.mode(datafile)

    return meanT, stdT, minvalT, modeT

def GSR_FD(clipid):#High fluctations of GSR_FD revals the phasic part of GSR.
    datafile=pd.read_csv('data_real/data'+clipid+'/ard_preprocessed.csv',index_col=0)
    first_diff=np.gradient(datafile["gsr"])

def HR_time(clipid):
    datafile=pd.read_csv('data_real/data'+clipid+'/hrv_preprocessed.csv',index_col=0)["hr"]

    meanHR=statistics.mean(hr)
    stdHR=statistics.stdev(hr)

    return meanHR,stdHR

def RR_time(clipid):

    #mean of all the standard deviations of RR intervals for all windows.

    diff_sucessives=[]

    rr=pd.read_csv('data_real/data'+clipid+'/hrv_preprocessed.csv',index_col=0)["rr"].to_numpy()

    meanRR = statistics.mean(rr)
    medianRR = statistics.median(rr)
    stdRR = statistics.stdev(rr)
    semRR = sem(rr)

    numjumps=0

    for i in range(1,len(rr)):
        diff_sucessives.append(rr[i]-rr[i-1])
        if rr[i]-rr[i-1]>=50:
            numjumps+=1

    fracjumps = numjumps/len(rr)

    rmsRR = np.square(np.mean(diff_sucessives))

    return meanRR, medianRR, stdRR, semRR, numjumps, fracjumps, rmsRR

def RR_bands(freqs,psd):

    iVLF=0
    iLF=0
    iHF=0

    for i in freqs:
        if i>0.04:
            break
        iVLF+=1

    for j in freqs[iVLF:]:
        if j>0.15:
            break
        iLF+=1

    for k in freqs[iLF:]:
        if k>0.5:
            break
        iHF+=1

    return [freqs[:iVLF],psd[:iVLF]], [freqs[iVLF:iLF],psd[iVLF:iLF]], [freqs[iLF:iHF],psd[iLF:iHF]]


def RR_freq(clipid):
    datafile=pd.read_csv('data_real/data'+clipid+'/hrv_preprocessed.csv',index_col=0)["rr"]
    freqs, psd = signal.welch(datafile)
    VLF,LF,HF=RR_bands(freqs,psd)

    maxVLF =np.amax(VLF)
    maxLF = np.amax(LF)
    maxHF = np.amax(HF)

    aVLF = np.sum(VLF)
    aLF = np.sum(LF)
    aHF = np.sum(HF)
    aTOT = aVLF+aLF+aHF

    pVLF = aVLF/aTOT
    pLF = aLF/aTOT
    pHF = aHF/aTOT

    nLF = aLF/(aLF+aHF)
    nHF = aHF/(aLF+aHF)

    LFHF = aLF/aHF


    return freqs, psd, maxVLF, maxLF, maxHF, aVLF, aLF, aHF, aTOT, pVLF, pLF, pHF, nLF, nHF, LFHF



"""plt.plot(RR_freq("s")[0],RR_freq("s")[1],label="Sadness")
plt.plot(RR_freq("h")[0],RR_freq("h")[1],label="Amusement")
plt.plot(RR_freq("t")[0],RR_freq("t")[1],label="Tenderness")
plt.plot(RR_freq("f")[0],RR_freq("f")[1],label="Fear")
plt.plot(RR_freq("b1")[0],RR_freq("b1")[1],label="base")
plt.legend()
plt.show()"""












