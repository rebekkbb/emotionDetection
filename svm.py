from sklearn import svm
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

y=[]
for i in range(8):
    for j in range(4):
        y.append(j)

df=pd.read_csv("featureMatrix.csv")

X=df.values

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state =50)



clf= svm.SVC(kernel='rbf', gamma=1, C=1, decision_function_shape='ovo').fit(X_train,y_train)
y_pred = clf.predict(X_test) 
print(clf.score(X_test,y_test))
print(confusion_matrix(y_test,y_pred))

