import numpy as np

def F(x):
    return np.cos(x) + x[::-1] - [1, 2, 3, 4]

import scipy.optimize
x = scipy.optimize.broyden1(F, [1,1,1,1], f_tol=1e-14)
print(x)
print(np.cos(x) + x[::-1])
#array([ 1.,  2.,  3.,  4.])