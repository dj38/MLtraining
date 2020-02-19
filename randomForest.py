import sklearn.ensemble as rf
from sklearn.datasets import load_breast_cancer
import sklearn.tree
import matplotlib.pyplot as plt

cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']

# print(X.shape) #569 * 30
# print(y.shape) #569

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)

import sklearn.neighbors as nn

optimal_nn = 1
optimal_score = 0
nnList= range(1, 30)
scoreList = []
model = rf.RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)
score = model.score(X_test, y_test)
print("score = " + str(score))

namePerf = list(zip(cancer.feature_names,model.feature_importances_))
namePerf.sort(key = lambda x: x[1], reverse=True)
# print(namePerf)

# print(model.feature_importances_)

plt.bar([n for n,w in namePerf[:10]] , [w for n,w in namePerf[:10]])
plt.show()

print(list(zip(cancer.feature_names,model.feature_importances_)))

estimator = model.estimators_[0]
print(estimator)

plt.figure()
sklearn.tree.plot_tree(estimator,
                feature_names = cancer.feature_names,
                class_names = cancer.target_names,
                rounded = True, proportion = False,
                precision = 2, filled = True)
# plt.show()
