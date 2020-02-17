import numpy as np
import matplotlib.pyplot as plt

# exemple de transformee de Fourrier

v = np.zeros(100)

v[1] = 1
print(v)
res = np.fft.fft(v)
print(res)
plt.plot(np.real(res))
plt.show()