# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 14:55:27 2018
DAY 6, MITE, MANGALORE
@author: pooja
"""
import sklearn


from sklearn.datasets import load_iris
data = load_iris()
import pandas as pd
from sklearn import preprocessing
# load the iris dataset
iris = load_iris()
print(iris.data.shape)
# separate the data from the target attributes
X = iris.data
y = iris.target
# normalize the data attributes
normalized_X = preprocessing.normalize(X)
standardized_X = preprocessing.scale(X)

from sklearn.preprocessing import MinMaxScaler
data = [[-1, 2], [-0.5, 6],[0, 10], [1, 18]]
scaler = MinMaxScaler()
print(scaler.fit(data))
#MinMaxScaler(copy=True, feature_range=(0, 1))
print(scaler.data_max_)
#[  1.  18.]
print(scaler.transform(data))
[[ 0.    0.  ]
 [ 0.25  0.25]
 [ 0.5   0.5 ]
 [ 1.    1.  ]]
print(scaler.transform([[2, 2]]))
[[ 1.5  0. ]]
data1=[[2,2]]
scaler.fit(data1)

http://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html
from sklearn import decomposition

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)





