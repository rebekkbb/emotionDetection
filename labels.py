import numpy as np
import pandas as pd
import featureExtractor



def calculateLabels(clipnum,participant):
	lengths=featureExtractor.lengths
	newvalence=[]
	newarousal=[]
	Q=[]
	scared=[]
	jumpscare=[]

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
			scared.append(0)
			jumpscare.append(0)
		elif (newvalence[j]>0 and newarousal[j]<0):
			Q.append(2)
			scared.append(0)
			jumpscare.append(0)
		elif (newvalence[j]<0 and newarousal[j]<0):
			Q.append(3)
			scared.append(0)
			jumpscare.append(0)
		elif (newvalence[j]<0 and newarousal[j]>0):
			Q.append(4)
			scared.append(1)
			if newarousal[j]>3.5:
				jumpscare.append(1)
			else:
				jumpscare.append(0)
		else:
			Q.append(0)
			scared.append(0)
			jumpscare.append(0)






	df = pd.DataFrame({'arousal': newarousal[:lengths[str(clipnum)]],'valence': newvalence[:lengths[str(clipnum)]],'Q':Q[:lengths[str(clipnum)]],'scared':scared[:lengths[str(clipnum)]],'jumpscare':jumpscare[:lengths[str(clipnum)]]})
	df.to_csv('data/labels/label_clip'+clipnum+'.csv')


#for i in range(2,22):
	#calculateLabels(str(i),'r')

for i in range(2,22):
	calculateLabels(str(i),'r')