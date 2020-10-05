import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage.restoration import denoise_wavelet
from scipy.signal import savgol_filter
import os

def denoiseSignal(clipNum):
    datafile=np.loadtxt("data/data"+clipNum+"/GSRvalues.txt",delimiter=',',skiprows=1)
    x=datafile[:,0]
    y=datafile[:,1]
    y_denoise = savgol_filter(y,101,2)
    arr_denoise = np.column_stack((x,y_denoise))

    try:
        os.remove('data/data'+clipNum+'/GSR_denoised.txt')
    except OSError:
        pass

    f=open('data/data'+clipNum+'/GSR_denoised.txt','a')
    f.write("time,gsr\n")
    np.savetxt(f,arr_denoise,delimiter=',')

    plt.plot(x,y)
    plt.plot(x,y_denoise)
    plt.show()


denoiseSignal('6')