import numpy as np

def create_data_sin(samples=10000):
   X = np.arange(samples).reshape(-1, 1) / samples
   y = np.sin(2 * np.pi * X).reshape(-1, 1)
   return X, y

import matplotlib.pyplot as plt

X, y = create_data_sin(samples=1000)
plt.scatter(X[:,0], y)
#plt.scatter(X[:,0], y, c=y, cmap="brg")

plt.show()
