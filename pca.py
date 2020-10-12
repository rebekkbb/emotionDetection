import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("data/data3/preprocessedData.txt",sep=',',skiprows=1)

data.columns=['time','hr','rr','ecg','gsr']

X = data[['hr','rr','ecg','gsr']].values
print(data.columns)

pca=PCA(2)
projected=pca.fit_transform(X)

plt.figure(figsize=(15,10))
plt.scatter(projected[:, 0],projected[:, 1], edgecolor='none',alpha=0.5,cmap=plt.cm.get_cmap('Spectral',10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar()

plt.show()


"""scaled_data = preprocessing.scale(datafile.T)
targets=np.array([0,1,2,3])

pca=PCA(2)
projected=pca.fit_transform(scaled_data)
print(projected.shape)
print(scaled_data.shape)

print(projected[:,0].T)


plt.figure(figsize=(15,10))
plt.scatter(projected[:, 0],projected[:, 1], c= targets, edgecolor='none',alpha=0.5,cmap=plt.cm.get_cmap('Spectral',10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar()

plt.show()



pca_data = pca.transform(scaled_data)

target_names = ['hr','rr','ecg','gsr']
colors=['navy','turquoise','darkorange','yellow']
lw=2


per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
labels = ['PC' + str(x) for x in range(1,len(per_var)+1)]
plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of explained variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

for color, i, target_name in zip(colors,[0,1,2,3],target_names):
    plt.scatter(pca_data[0],pca_data[1], color=color, alpha=.8, lw=lw, label=target_name)

plt.show()"""
