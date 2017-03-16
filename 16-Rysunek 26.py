from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-40, 40, 0.1)
Y = np.arange(-40, 40, 0.1)
X, Y = np.meshgrid(X, Y)
#https://en.wikipedia.org/wiki/Rosenbrock_function
N = 0
for i in range(-2,3):
	for j in range(-2,3):
		TEMP = (5 * (i + 2) + j + 3 + (X - 16 * j)**6 + (Y - 16 * i)**6)**-1
		N = N + TEMP
Z = (N+0.002)**-1
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()