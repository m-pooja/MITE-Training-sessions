#load data
import pandas as pd
#from pandas.tools.plotting import parallel_coordinates
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names=['sepal_length','sepal_width','petal_length','petal_width','label']
iris_data=pd.read_csv(url,names=names)

#dimension
iris_data.shape

#to look inside data
iris_data.head()

#statistical summary
iris_data.describe()

#find class distribution
iris_data.groupby('label').size()

#univariate analysis
import matplotlib as plt  
iris_data.hist()
iris_data.plot(kind='box',subplots=True,sharex=False,sharey=False)

#multivariate analysis
from pandas.tools.plotting import scatter_matrix
scatter_matrix(iris_data)

array=iris_data.values
x=array[:,0:4]
y=array[:,4]

#splitting the data into train and test
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=.20, random_state=7)

"""KNN"""
#model 
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)

#predict
predictions=knn.predict(x_test)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test,predictions))

"""logistic regression"""
from sklearn.linear_model import LinearRegression, LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
predicts=lr.predict(x_test)
print(accuracy_score(y_test,predicts))
print(confusion_matrix(y_test, predicts))
print(classification_report(y_test,predicts))

"""decision trees"""
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
pred=dt.predict(x_test)
print(accuracy_score(y_test,pred))
print(confusion_matrix(y_test, pred))
print(classification_report(y_test,pred))

"""Navie Bayes"""
from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(x_train,y_train)
pre=nb.predict(x_test)
print(accuracy_score(y_test,pre))
print(confusion_matrix(y_test, pre))
print(classification_report(y_test,pre))

"""Multinomail Navie Bayes"""
from sklearn.naive_bayes import MultinomialNB
nb1=MultinomialNB()
nb1.fit(x_train,y_train)
pre1=nb1.predict(x_test)
print(accuracy_score(y_test,pre1))
print(confusion_matrix(y_test, pre1))
print(classification_report(y_test,pre1))

"""KMeans"""
from sklearn.cluster import KMeans
import numpy as np
from sklearn.datasets import load_iris
iris_data=load_iris()
data=iris_data.data
target=iris_data.target
iris_data.head()
x1=data[:,0]
x2=data[:,1]
import matplotlib.pyplot as plt
plt.plot()
import numpy as np
plt.xlim([np.min(x1),np.max(x1)])
plt.ylim([np.min(x2),np.max(x2)])
plt.title('iris_data')
plt.scatter(x1,x2)
plt.show()

plt.plot()
X=np.array(list(zip(x1,x2))).reshape(len(x1),2)
colors=['b','g','r']
markers=['o','v','s']

#KMeans algorithm
K=3
k=KMeans(n_clusters=3).fit(X)
plt.plot()
for i ,l in enumerate(k.labels_):
    plt.plot(x1[i],x2[i],
             color=colors[l],
        marker=markers[l], ls='None')
    plt.xlim([np.min(x1),np.max(x1)])
    plt.ylim([np.min(x2),np.max(x2)])
    
    
plt.show()

"""Random Forest"""
from sklearn.ensemble import RandomForestClassifier
rd=RandomForestClassifier(n_jobs=2)
RF=rd.fit(x_train,y_train)
pre_rd=rd.predict(x_test)
print(accuracy_score(y_test,pre_rd))
print(confusion_matrix(y_test, pre_rd))
print(classification_report(y_test,pre_rd))

"""Dumping the model"""   #(saving our models)
#joblib
from sklearn.externals import joblib
joblib.dump(k,"myK.model",compress=5)
#calling model
model=joblib.load("myK.model")
model.predict(x_test)
model.close
"""pickle"""
import pickle
mymodel=open("RF.model",'wb')
pickle.dump(k,mymodel)



mymodel=open("RF.model",'rb')

m=pickle.load(mymodel)


















