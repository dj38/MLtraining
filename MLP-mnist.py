import numpy as np
import sklearn.neural_network
import matplotlib.pyplot as plt

with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']

print(type(x_train))

sample = np.random.randint(60000, size=100)
x_train = x_train[sample]
y_train = y_train[sample]

# On redimensionne les données
x_train = x_train.reshape((-1, 784))
x_test = x_test.reshape((-1, 784))

model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(784,300,100), max_iter=10000)
model.fit(x_train,y_train)
score = model.score(x_test,y_test)
print("MLP score : %f" % score)

predicted = model.predict(x_test)

x1 = x_test[range(20)]
y1 = y_test[range(20)]
x1Predict = model.predict(x1)
print(x1.shape)
x1False = x1[np.where([xv==yv for (xv,yv) in zip(y1,x1Predict)])
print(x1False.shape)

# x_false = [xv if model.predict(xv) for (c,xv,yv) in zip(condition,x,y)]
x_test = x_test.reshape((-1, 28, 28))

# On selectionne un echantillon de 12 images au hasard
select = np.random.randint(x_test.shape[0], size=12)

# On affiche les images avec la prédiction associée
for index, value in enumerate(select):
    plt.subplot(3, 4, index + 1)
    plt.axis('off')
    plt.imshow(x_test[value], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title("Pred/Targ: " + str(predicted[value]) + "/" + str(y_test[value]))

plt.show()
