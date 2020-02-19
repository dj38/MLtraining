from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import os
os.environ['CUDA_VISIBLE_DEVICES']='-1'

cancer = load_breast_cancer()
X = cancer['data']
y = cancer['target']



X_train,X_test,y_train,y_test = train_test_split(X,y)

# Multi layer perceptrion avec Scaling (avg a 0 et StdDev=1)
scaler = StandardScaler()
scaler.fit(X_train)
X_trainScaled = scaler.transform(X_train)
X_testScaled = scaler.transform(X_test)

import tensorflow.keras as keras

model = keras.Sequential([
    keras.layers.Dense(30, input_shape=(X_trainScaled.shape[1],)),
    keras.layers.Dense(1)
])

model.compile(loss="mse")
model.summary()

# validation_split permet de separer donnees de train et test directement dans le model
history = model.fit(X_trainScaled, y_train, epochs=100, batch_size = 1)
score = model.evaluate(X_testScaled, y_test)
print("score : %f " % score)
