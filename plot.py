import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import featureExtractor2




#emotions plots
t = pd.read_csv("data_real/datat/ard_preprocessed.csv")
f = pd.read_csv("data_real/dataf/ard_preprocessed.csv")
h = pd.read_csv("data_real/datah/ard_preprocessed.csv")
s = pd.read_csv("data_real/datas/ard_preprocessed.csv")

b1 = pd.read_csv("data_real/datat/ard_preprocessed.csv")
b2 = pd.read_csv("data_real/dataf/ard_preprocessed.csv")
b3 = pd.read_csv("data_real/datah/ard_preprocessed.csv")
b4 = pd.read_csv("data_real/datah/ard_preprocessed.csv")

plt.plot(np.arange(len(t["gsr"])),t["gsr"],label="Tenderness")
plt.plot(np.arange(len(f["gsr"])),f["gsr"],label="Fear")
plt.plot(np.arange(len(s["gsr"])),s["gsr"],label="Sadness")
plt.plot(np.arange(len(h["gsr"])),h["gsr"],label="Amusement")
plt.legend()
plt.show()

#Baselines+ cogsresponding emotion

plt.plot(np.arange(len(b1["gsr"])),b1["gsr"],label="Amusement-baseline")
plt.plot(np.arange(len(h["gsr"])),h["gsr"],label="Amusement")
plt.legend()
plt.show()

plt.plot(np.arange(len(b2["gsr"])),b2["gsr"],label="Sadness-baseline")
plt.plot(np.arange(len(s["gsr"])),s["gsr"],label="sadness")
plt.legend()
plt.show()

plt.plot(np.arange(len(b3["gsr"])),b3["gsr"],label="Fear-baseline")
plt.plot(np.arange(len(f["gsr"])),f["gsr"],label="Fear")
plt.legend()
plt.show()

plt.plot(np.arange(len(b4["gsr"])),b4["gsr"],label="Tenderness-baseline")
plt.plot(np.arange(len(t["gsr"])),t["gsr"],label="Tenderness")
plt.legend()
plt.show()



#baselines plots


#PSD plots

"""plt.plot(featureExtractor2.gsr_freq("s")[0],featureExtractor2.gsr_freq("s")[1],label="Sadness")
plt.plot(featureExtractor2.gsr_freq("h")[0],featureExtractor2.gsr_freq("h")[1],label="Amusement")
plt.plot(featureExtractor2.gsr_freq("t")[0],featureExtractor2.gsr_freq("t")[1],label="Tenderness")
plt.plot(featureExtractor2.gsr_freq("f")[0],featureExtractor2.gsr_freq("f")[1],label="Fear")
plt.legend()
plt.show()

plt.plot(x,y)
plt.legend()
plt.show()"""
