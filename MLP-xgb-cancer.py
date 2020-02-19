import numpy as np
import sklearn.neural_network
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import math
import xgboost as xgb

def runModel(model, modelName, Xtrain, ytrain, Xtest, ytest) :
    print("Running model " + modelName)
    model.fit(Xtrain, ytrain)
    score = model.score(Xtest, ytest)
    print("\tScore : %f" % score)

#input
cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2
X=cancer['data']
y=cancer['target']
# print(X.shape) #569 * 30
# print(y.shape) #569
X_train,X_test,y_train,y_test = train_test_split(X,y)

# Multi layer perceptron sans scaling
model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(30,15), max_iter=10000)
runModel(model,"MLP noScale",X_train,y_train,X_test,y_test)

# Multi layer perceptrion avec Scaling (avg a 0 et StdDev=1)
scaler = StandardScaler()
scaler.fit(X_train)
X_trainScaled = scaler.transform(X_train)
X_testScaled = scaler.transform(X_test)
# print(scaler.mean_)
# print([math.sqrt(x) for x in scaler.var_])
# print(scaler.transform(X_train))
runModel(model,"MLP with Scale",X_trainScaled,y_train,X_testScaled,y_test)

# xgboost
model = xgb.XGBClassifier(n_estimators=100)
runModel(model,"xgboost",X_trainScaled,y_train,X_testScaled,y_test)
xgb.plot_importance(model)
# xgb.plot_tree(model)
plt.show()
