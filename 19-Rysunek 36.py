from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-30, 50, 0.1)
Y = np.arange(-30, 50, 0.1)
X, Y = np.meshgrid(X, Y)
#https://en.wikipedia.org/wiki/Rosenbrock_function
hasilke1 = []
for i in range(1,30):
    hasilke1.append((((X - i)**2) + ((Y-i)**2) + i)**-1)
Z = (-1) * (sum(hasilke1))
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()