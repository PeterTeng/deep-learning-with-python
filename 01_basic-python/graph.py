import numpy as np
import matplotlib.pyplot as plt

# Set data
x = np.arange(0, 10, 0.1) # 0 to 6 with 0.1 interval

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin and cos")
plt.legend()
plt.show()
