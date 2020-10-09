import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage.restoration import denoise_wavelet
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
import os



def interpolateNaN(y):
    ok = ~np.isnan(y)
    xp = ok.ravel().nonzero()[0]
    fp = y[~np.isnan(y)]
    x  = np.isnan(y).ravel().nonzero()[0]
    y[np.isnan(y)] = np.interp(x, xp, fp)
    return y

def preprosess(clipnum):
    xgsr=np.loadtxt("data/data"+clipnum+"/GSRvalues.txt",delimiter=',',skiprows=1)[:,0]
    ygsr=np.loadtxt("data/data"+clipnum+"/GSRvalues.txt",delimiter=',',skiprows=1)[:,1]

    xhr = np.loadtxt("data/data"+clipnum+"/values.txt",delimiter=',',skiprows=1)[:,0]
    yhr = np.loadtxt("data/data"+clipnum+"/values.txt",delimiter=',',skiprows=1)[:,1]

    yrr = np.loadtxt("data/data"+clipnum+"/values.txt",delimiter=',',skiprows=1)[:,2]

    xecg= np.loadtxt("data/data"+clipnum+"/ECGvalues.txt",delimiter=',',skiprows=1)[:,0]
    yecg= np.loadtxt("data/data"+clipnum+"/ECGvalues.txt",delimiter=',',skiprows=1)[:,1]

    yrr_nonan=interpolateNaN(yrr)

    try:
        os.remove('data/data'+clipnum+'preprocessedData.txt')
    except OSError:
        pass

    f = open('data/data'+clipnum+'/preprocessedData.txt','a')
    f.write("time,hr,rr,ecg,gsr\n")

    ggsr= interp1d(xgsr, ygsr, kind='previous', bounds_error=False)
    ghr= interp1d(xhr, yhr, kind='previous', bounds_error=False)
    grr= interp1d(xhr, yrr_nonan, kind='previous', bounds_error=False)

    preprosGSR=savgol_filter(ggsr(xecg),101,2)
    alldata=np.column_stack((xecg,ghr(xecg),grr(xecg),yecg,preprosGSR))
    np.savetxt(f,alldata,delimiter=',')
preprosess("2")


