import statistics
import numpy as np
from scipy.stats import linregress, kurtosis, skew, sem
import pandas as pd
import math
from scipy import signal
import matplotlib.pyplot as plt

def GSRfeatures(clipid,participant):
    datafile=pd.read_csv('data_real/P'+participant+'/data'+clipid+'/ard_preprocessed.csv',index_col=0)["gsr"]

    meanGSR = statistics.mean(datafile)
    stdGSR = statistics.stdev(datafile)
    slopeGSR, interceptGSR, r_valueGSR, p_valueGSR, std_errGSR = linregress(datafile.index,datafile)
    maxvalGSR = max(datafile)
    minvalGSR = min(datafile)
    #modeGSR = statistics.mode(datafile)
    kurtosisGSR = kurtosis(datafile)
    skewnessGSR = skew(datafile)

    return meanGSR, stdGSR, slopeGSR, maxvalGSR, minvalGSR, kurtosisGSR, skewnessGSR

def Tempfeatures(clipid,participant):
    datafile=pd.read_csv('data_real/P'+participant+'/data'+clipid+'/ard_preprocessed.csv',index_col=0)["temp"]

    meanT=statistics.mean(datafile)
    stdT=statistics.stdev(datafile)
    minvalT=min(datafile)
    maxvalT=max(datafile)
    modeT=statistics.mode(datafile)

    return meanT, stdT, minvalT, maxvalT, modeT

def GSR_FD(clipid,participant):#High fluctations of GSR_FD revals the phasic part of GSR.
    datafile=pd.read_csv('data_real/P'+participant+'/data'+clipid+'/ard_preprocessed.csv',index_col=0)
    first_diff=np.gradient(datafile["gsr"])
    GSRFDsqrtMean = np.sqrt(np.mean(first_diff**2))
    GSRFDmean = np.mean(first_diff)

    return GSRFDsqrtMean, GSRFDmean

def HR_time(clipid,participant):
    hr=pd.read_csv('data_real/P'+participant+'/data'+clipid+'/hrv_preprocessed.csv',index_col=0)["hr"]

    meanHR=statistics.mean(hr)
    stdHR=statistics.stdev(hr)

    return meanHR,stdHR

def RR_time(clipid,participant):

    #mean of all the standard deviations of RR intervals for all windows.

    diff_sucessives=[]

    rr=pd.read_csv('data_real/P'+participant+'/data'+clipid+'/hrv_preprocessed.csv',index_col=0)["rr"].to_numpy()

    meanRR = statistics.mean(rr)
    medianRR = statistics.median(rr)
    stdRR = statistics.stdev(rr)
    semRR = sem(rr)

    numjumps=0

    for i in range(1,len(rr)):
        diff_sucessives.append(rr[i]-rr[i-1])
        if rr[i]-rr[i-1]>=50:
            numjumps+=1

    RRfracjumps = numjumps/len(rr)

    rmsRR = np.square(np.mean(diff_sucessives))

    return meanRR, medianRR, stdRR, semRR, RRfracjumps, rmsRR



def RR_freq(clipid,participant):
    datafile=pd.read_csv('data_real/P'+participant+'/data'+clipid+'/hrv_preprocessed.csv',index_col=0)["rr"]
    freqs, psd = signal.welch(datafile,nperseg=170)
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


    return maxVLF, maxLF, maxHF, aVLF, aLF, aHF, aTOT, pVLF, pLF, pHF, nLF, nHF, LFHF


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

participants=[1,2,3,4,5,6,7,8]
clips=["FA","FF","FS","FT"]
df = pd.DataFrame(columns = ["meanGSR", "stdGSR", "slopeGSR", "maxvalGSR", "minvalGSR", "kurtosisGSR", "skewnessGSR","GSRFDsqrtMean", "GSRFDmean","meanHR","stdHR","meanRR", "medianRR", "stdRR", "semRR", "RRfracjumps", "rmsRR", "maxVLF", "maxLF", "maxHF", "aVLF", "aLF", "aHF", "aTOT", "pVLF", "pLF", "pHF", "nLF", "nHF", "LFHF"])
print(df)
for p in participants:
    for d in clips:
        meanGSR, stdGSR, slopeGSR, maxvalGSR, minvalGSR, kurtosisGSR, skewnessGSR = GSRfeatures(d,str(p))
        print (meanGSR)
        meanT, stdT, minvalT, maxvalT, modeT = Tempfeatures(d,str(p))
        GSRFDsqrtMean, GSRFDmean = GSR_FD(d,str(p))
        meanHR,stdHR = HR_time(d,str(p))
        meanRR, medianRR, stdRR, semRR, RRfracjumps, rmsRR = RR_time(d,str(p))
        maxVLF, maxLF, maxHF, aVLF, aLF, aHF, aTOT, pVLF, pLF, pHF, nLF, nHF, LFHF = RR_freq(d,str(p))
        df=df.append({"meanGSR" : meanGSR, "stdGSR": stdGSR, "slopeGSR":slopeGSR, "maxvalGSR":maxvalGSR, "minvalGSR":minvalGSR, "kurtosisGSR":kurtosisGSR, "skewnessGSR":skewnessGSR,"GSRFDsqrtMean":GSRFDsqrtMean, "GSRFDmean":GSRFDmean,"meanHR":meanHR,"stdHR":stdHR,"meanRR":meanRR, "medianRR":medianRR, "stdRR":stdRR, "semRR":semRR, "RRfracjumps":RRfracjumps, "rmsRR":rmsRR, "maxVLF":maxVLF, "maxLF":maxLF, "maxHF":maxHF, "aVLF":aVLF, "aLF":aLF, "aHF":aHF, "aTOT":aTOT, "pVLF":pVLF, "pLF":pLF, "pHF":pHF, "nLF":nLF, "nHF":nHF, "LFHF":LFHF},ignore_index=True)



df.to_csv("featureMatrix.csv")


"""plt.plot(RR_freq("s")[0],RR_freq("s")[1],label="Sadness")
plt.plot(RR_freq("h")[0],RR_freq("h")[1],label="Amusement")
plt.plot(RR_freq("t")[0],RR_freq("t")[1],label="Tenderness")
plt.plot(RR_freq("f")[0],RR_freq("f")[1],label="Fear")
plt.plot(RR_freq("b1")[0],RR_freq("b1")[1],label="base")
plt.legend()
plt.show()"""












