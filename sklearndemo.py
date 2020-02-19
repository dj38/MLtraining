import pandas as pd
import sklearn.linear_model as sklm
import numpy as np

data = pd.read_csv('data/house/house.csv')
regr = sklm.LinearRegression()
X = data["surface"].values.reshape(-1,1)
y = data["loyer"]
regr.fit(X,y)
print(regr.predict(X))
print(regr.score(X, y))
print(regr.coef_)
print(regr.intercept_)

import matplotlib.pyplot as plt
# plt.plot(data["surface"], data["loyer"], 'ro', markersize=4)
# plt.plot(data["surface"], regr.predict(X) )
# plt.show()

import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.model_selection as ms

# make_pipe_line create a model with a feature
# PolynomialFeature = Algo polynomial
# Ridge = Error square algo
# model = pp.make_pipeline(pipe.PolynomialFeatures(1), sklm.Ridge())
# <=> LinearRegression

# separation du jeu d'apprentissage et jeu de test
# a faire dans tous les projets de machine learning !!!!
# si appel a un sous traitant, le jeu de test pour la recette ne doit pas lui etre communique...
xtrain, xtest, ytrain, ytest = ms.train_test_split(X, y , train_size=0.8, test_size=0.2)

model = pipe.make_pipeline(pp.PolynomialFeatures(2), sklm.Ridge())
xtrain = xtrain.reshape(-1,1)
model.fit(xtrain,ytrain)
X_plot = np.arange(400).reshape(-1,1)
print("Model score : " + str(model.score(xtest,ytest)))
y_plot = model.predict(X_plot)
plt.scatter(xtrain, ytrain, s=4)
plt.scatter(xtest, ytest, s=4)
plt.plot(X_plot, y_plot)
plt.show()
import math
print(model.score(X, y))
