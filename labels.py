import numpy as np
import pandas as pd
import preprocessing


def calculateLabels(clipnum,participant):
	lengths=preprocessing.cliplengths
	newvalence=[]
	newarousal=[]
	Q=[]

	arousal = np.loadtxt("data/labels/"+clipnum+"_temperal.txt", delimiter='\t')[0]
	valence = np.loadtxt("data/labels/"+clipnum+"_temperal.txt", delimiter='\t')[1]



	for i in range(len(arousal)-1):
		newarousal.extend([arousal[i],arousal[i]*(4/5)+arousal[i+1]*(1/5),arousal[i]*(3/5)+arousal[i+1]*(2/5),arousal[i]*(2/5)+arousal[i+1]*(3/5),arousal[i]*(1/5)+arousal[i+1]*(4/5)])
		newvalence.extend([valence[i],valence[i]*(4/5)+valence[i+1]*(1/5),valence[i]*(3/5)+valence[i+1]*(2/5),valence[i]*(2/5)+valence[i+1]*(3/5),valence[i]*(1/5)+valence[i+1]*(4/5)])

	newarousal.extend([arousal[-1]]*5)
	newvalence.extend([valence[-1]]*5)


	for j in range(len(newvalence)):
		if (newvalence[j]>0 and newarousal[j]>0):
			Q.append(1)
		elif (newvalence[j]>0 and newarousal[j]<0):
			Q.append(2)
		elif (newvalence[j]<0 and newarousal[j]<0):
			Q.append(3)
		elif (newvalence[j]<0 and newarousal[j]>0):
			Q.append(4)
		else:
			Q.append(0)






	df = pd.DataFrame({'arousal': newarousal[:lengths[str(clipnum)]],'valence': newvalence[:lengths[str(clipnum)]],'Q':Q[:lengths[str(clipnum)]]})
	df.to_csv('data/labels/label_clip'+clipnum+'.csv')


#for i in range(2,22):
	#calculateLabels(str(i),'r')

for i in range(2,22):
	calculateLabels(str(i),'r')