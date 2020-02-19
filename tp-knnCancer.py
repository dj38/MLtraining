from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']

print(X.shape) #569 * 30
print(y.shape) #569

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)

import sklearn.neighbors as nn

optimal_nn = 1
optimal_score = 0
nnList= range(1, 30)
scoreList = []
for n in range(1,30):
    model = nn.KNeighborsClassifier(n_neighbors=n)
    model.fit(X_train,y_train)
    score = model.score(X_test, y_test)
    print("For n = " + str(n) + ", score = " + str(score))
    scoreList.append(score)
    if optimal_score < score:
        optimal_score = score
        optimal_nn = n

print("\nOptimal score for n = " + str(optimal_nn) + ", score = " + str(optimal_score))

import matplotlib.pyplot as plt

plt.plot(nnList, scoreList)
plt.show()