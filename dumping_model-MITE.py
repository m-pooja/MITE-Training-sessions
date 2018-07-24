"""Dumping the model"""   #(saving our models)
#joblib
from sklearn.externals import joblib
joblib.dump(RF,"RF.model",compress=5)
model=joblib.load("RF.model")
model.predict(x_test)
model.close


"""pickle"""
import pickle
mymodel=open("RF.model",'wb')
pickle.dump()
