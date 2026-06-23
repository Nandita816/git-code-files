import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

plt.hexbin(x, y, gridsize=20, cmap='Greens')

cb = plt.colorbar()

plt.show()