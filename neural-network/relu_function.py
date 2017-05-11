import numpy as np
import matplotlib.pylab as plt

# Easy way
def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.2, 1.2)
plt.show()
