import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde
from matplotlib.colors import ListedColormap
 
# Create data: 200 points
data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 3]], 500)
x, y = data.T

print(data[0])

cmap = plt.cm.OrRd

# Get the colormap colors
my_cmap = cmap(np.arange(cmap.N))

# Set alpha
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)

# Create new colormap
my_cmap = ListedColormap(my_cmap)

img = plt.imread("test.png")

# Create a figure with 6 plot areas
fig, axes = plt.subplots(ncols=4, nrows=1, figsize=(21, 5))
 
# Everything sarts with a Scatterplot
axes[0].set_title('Scatterplot')
axes[0].plot(x, y, 'ko', alpha=0.5)
# As you can see there is a lot of overplottin here!
 
# Thus we can cut the plotting window in several hexbins
nbins = 20
axes[1].set_title('Hexbin')
axes[1].hexbin(x, y, gridsize=nbins, cmap=my_cmap)
 
# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
k = kde.gaussian_kde(data.T)
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
 
# plot a density
axes[2].set_title('Calculate Gaussian KDE')
axes[2].pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=my_cmap)
 
# add shading
axes[3].set_title('2D Density with shading')
axes[3].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=my_cmap)


axes[0].imshow(img, extent=[-5, 3, -5, 3])
axes[1].imshow(img, extent=[-5, 3, -5, 3])
axes[2].imshow(img, extent=[-5, 3, -5, 3])
axes[3].imshow(img, extent=[-5, 3, -5, 3])

plt.show(fig)