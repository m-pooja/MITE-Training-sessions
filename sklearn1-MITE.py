# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:33:50 2018
DAY7, MITE, MANGALORE
@author: pooja
"""
#Prediction of Quality ranking of the wines and Evaluate the performance of any two models of your choice on provided wine_dataset.
#Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import SKlearn
from sklearn.datasets import load_iris
#Load the dataset
dataset=pd.read_excel("Wine_data.xlsx")

#check for unique values in dependent variable
dataset['quality'].unique()#3-9

dataset.head()

dataset.tail()

#To find the statistical summary
dataset.describe()

#Univariate Analysis
dataset.hist()

#Multivariate Analysis
from pandas.tools.plotting import scatter_matrix

pd.scatter_matrix(dataset)

#Group the dependent variable and independent variables
array=dataset.values
X=array[:,0:11]
Y=array[:,11]

#Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#sc_y = StandardScaler()
#Y_train = sc_y.fit_transform(Y_train)



#Fitting the classifier to the training set using LogisticRegression
from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(X_train,Y_train)

#Predicting the test set results
y_pred=lr.predict(X_test)

#Confusion Matrix,Accuracy and Classification Report
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

print(confusion_matrix(Y_test,y_pred))

print(accuracy_score(Y_test,y_pred))#50%

print(classification_report(Y_test,y_pred))

