from sklearn import svm
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

featuresConcat = pd.DataFrame(columns=['meanTemp','stdTemp','meanNN','stdNN','NNnumjump','rootjumps','meanHR','stdHR'])
labelsConcat = pd.DataFrame(columns=['jumpscare'])

for i in [12,15,20,21]:
	datafile=pd.read_csv('data/r/features/features_clip'+str(i)+'.csv',index_col=0)
	labels=pd.read_csv('data/labels/label_clip'+str(i)+'.csv',usecols=['jumpscare'])
	featuresConcat=featuresConcat.append(datafile)
	labelsConcat=labelsConcat.append(labels)

X=featuresConcat.values
y=labelsConcat.values.flatten()
y=y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)


svclassifier = svm.SVC(kernel='rbf')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))




