import statistics
import numpy as np
from scipy.stats import linregress
import pandas as pd
import math
import preprocessing

lengths={}
clipnums=[2,4,17,18,19]

def GSRfeatures(clipnum,participant):
    datafile=pd.read_csv('data/'+participant+'/data'+clipnum+'/preprocessedData.csv',index_col=0)
    k=datafile.index[0]

    mean5sec = []
    std5sec = []
    slopes5sec = []
    intercept5sec = []
    max5sec = []
    min5sec = []

    while(k<=datafile.index[-1]):
        gsr5sec=datafile.loc[k:k+5]["gsr"].tolist()
        x5sec=datafile.loc[k:k+5].index.tolist()
        mean5sec.append(statistics.mean(gsr5sec))
        std5sec.append(statistics.stdev(gsr5sec))
        max5sec.append(max(gsr5sec))
        min5sec.append(min(gsr5sec))

        slope, intercept, r_value, p_value, std_err = linregress(x5sec,gsr5sec)

        slopes5sec.append(slope)

        k=k+1

    return mean5sec,std5sec,slopes5sec,max5sec,min5sec

def HRVfeatures(clipnum,participant):
    meanNN5sec = []
    medianNN5sec = []
    stdNN5sec = []
    NNnumjump5sec = []
    rootjumps = []
    meanHR5sec = []
    stdHR5sec = []

    datafile=pd.read_csv('data/'+participant+'/data'+clipnum+'/preprocessedData.csv',index_col=0)
    k=datafile.index[0]

    while(k<=datafile.index[-1]):
        rr5sec=datafile.loc[k:k+5]["rr"].tolist()
        hr5sec=datafile.loc[k:k+5]["hr"].tolist()

        meanNN5sec.append(statistics.mean(rr5sec))
        medianNN5sec.append(statistics.median(rr5sec))
        stdNN5sec.append(statistics.stdev(rr5sec))

        meanHR5sec.append(statistics.mean(hr5sec))
        stdHR5sec.append(statistics.stdev(hr5sec))

        jumps=[x - rr5sec[i - 1] for i, x in enumerate(rr5sec)][1:]
        negjumps=[abs(x) for x in jumps if x < 0 ]
        suma=sum(negjumps)
        rootjumps.append(math.sqrt(suma))
        bigjumps=[x for x in jumps if x <= -50 ]
        NNnumjump5sec.append(len(bigjumps))

        k+=1
    
    return meanNN5sec, medianNN5sec, stdNN5sec, NNnumjump5sec, rootjumps, meanHR5sec, stdHR5sec


def Tempfeatures(clipnum,participant):
    meanTemp5sec=[]
    stdTemp5sec=[]

    datafile=pd.read_csv('data/'+participant+'/data'+clipnum+'/preprocessedData.csv',index_col=0)
    k=datafile.index[0]

    while(k<=datafile.index[-1]):
        temp5sec=datafile.loc[k:k+5]["temperature"].tolist()
        meanTemp5sec.append(statistics.mean(temp5sec))
        stdTemp5sec.append(statistics.stdev(temp5sec))

        k+=1
    return meanTemp5sec, stdTemp5sec


   
for i in clipnums:
    meanTemp,stdTemp=Tempfeatures(str(i),'k')
    meanNN, medianNN, stdNN, NNnumjump, rootjumps, meanHR, stdHR=HRVfeatures(str(i),'k')
    meanGSR,stdGSR,slopesGSR,maxGSR,minGSR=GSRfeatures(str(i),'k')

    df=pd.DataFrame({'meanTemp': meanTemp,'stdTemp': stdTemp, 'meanNN':meanNN, 'stdNN': stdNN, 'NNnumjump': NNnumjump, 'rootjumps': rootjumps, 'meanHR':meanHR, 'stdHR':stdHR})
    lengths[str(i)]=len(df)
    df.to_csv('data/k/features/features_clip'+str(i)+'.csv')



  



