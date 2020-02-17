# np est l'alias par defaut pour numpy
import numpy as np

v1 = np.array([1,2,3,4])
v2 = np.arange(4)
print(v1+v2)
print(v1*v2)
print(np.sin(v1))

# a voir :
# np.eye
# np.diag , .zeros, .ones , .rand

# attention :  le . est present pour signifier qu'on travaille sur une matrice de float
mat1 = np.array([[1.,2,3],[10,20,30]])
mat2 = np.array([[1,2,3,4]],float).reshape(2,2)
print(mat1)
print(mat1.shape)

# transformation d'un vecteur en une matrice et inversement
print(v1.reshape(2,2))
print(mat1.reshape(6))
print(mat2)
# inversion de matrice
print(np.linalg.inv(mat2))
print(np.mean(np.random.rand(1025)))

# multiplication membre a membre
print(np.array([1,2]) * np.array([3,4]))
# produit de 2 matrices
print(np.array([1,2]).dot(np.array([3,4])))