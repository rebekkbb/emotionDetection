import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage.restoration import denoise_wavelet
from scipy.signal import savgol_filter
import os

datafile=np.loadtxt("data/data4/GSRvalues.txt",delimiter=',',skiprows=1)
x=datafile[:,0]
y=datafile[:,1]
y_denoise = savgol_filter(y,101,2)
arr_denoise = np.column_stack((x,y_denoise))
print(arr_denoise)

os.remove('data/data4/GSR_denoised.txt')
f=open('data/data4/GSR_denoised.txt','a')
f.write("time,gsr\n")
np.savetxt(f,arr_denoise,delimiter=',')
plt.plot(x,y)
plt.plot(x,y_denoise)
plt.show()