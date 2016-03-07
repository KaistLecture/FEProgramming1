

import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.linspace(0, 4, 13)
y = np.array([0, 2, 3, 3.5, 3.75, 3.875, 3.9375, 4])
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi*X/2) * np.exp(Y/2)

x2 = np.linspace(0, 4, 65)
y2 = np.linspace(0, 4, 65)
f = interp2d(x, y, Z, kind='quintic')
Z2 = f(x2, y2)

fig = plt.figure(figsize=(9,6))
ax0 = fig.add_subplot(121, projection='3d')
ax1 = fig.add_subplot(122, projection='3d')

ax0.plot_surface(X, Y, Z, cstride=1, rstride=1, cmap=cm.coolwarm)

X2, Y2 = np.meshgrid(x2, y2)
ax1.plot_surface(X2, Y2, Z2, cstride=5, rstride=5, cmap=cm.coolwarm)

fig.suptitle(r"$z(x,y) = \sin\left(\frac{\pi x}{2}\right)e^{y/2}$", fontsize=20)
fig.show()
