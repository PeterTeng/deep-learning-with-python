import numpy as np
import matplotlib.pyplot as plt

# Set data
x = np.arange(0, 10, 0.1) # 0 to 6 with 0.1 interval
y = np.sin(x)

plt.plot(x, y)
plt.show()
