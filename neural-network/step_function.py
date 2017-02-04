import numpy as np
import matplotlib.pylab as plt

# Easy way
def easy_step_function(x):
    if x > 0:
        return 1;
    else:
        return 0;

def ste_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.05)
y = ste_function(x)
plt.plot(x, y)
plt.ylim(-0.2, 1.2)
plt.show()
