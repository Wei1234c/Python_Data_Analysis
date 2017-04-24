import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20)

plt.plot(x,  .5 + x)
plt.plot(x, 1 + 2 * x, '--')
plt.show()
