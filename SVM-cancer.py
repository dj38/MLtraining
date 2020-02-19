import sklearn.svm as svm
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']
print(X.shape) #569 * 30
print(y.shape) #569
X_train,X_test,y_train,y_test = train_test_split(X,y)

model = svm.SVC(C=0.1, kernel="poly")
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print("Score : %f" %(score))