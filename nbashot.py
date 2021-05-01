#Game ID
#Game Event ID
#Player ID
#Player Name
#Team ID
#Team Name
#Period
#Minutes Remaining
#Seconds Remaining
#Action Type
#Shot Type
#Shot Zone Basic
#Shot Zone Area
#Shot Zone Range
#Shot Distance
#X Location
#Y Location
#Shot Made Flag
#Game Date
#Home Team
#Away Team
#Season Type

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde
from matplotlib.colors import ListedColormap

data = []

player_name = input("Enter player name: ")
print(f"\n\nGetting shot location for {player_name}...\n\n")

reader = csv.reader(open(r"db-locations.csv"), delimiter=',')
filtered = filter(lambda p: player_name == p[3] and '1' == p[17], reader)

for row in filtered:
    data.append([row[15], row[16]])

data = np.array(data).astype(np.float) # convert to numpy array. convert to float as well, while we are here...
x, y = data.T

cmap = plt.cm.OrRd

# Get the colormap colors
my_cmap = cmap(np.arange(cmap.N))

# Set alpha
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)

# Create new colormap
my_cmap = ListedColormap(my_cmap)

img = plt.imread("nba_court.png")

# Create a figure with 6 plot areas
fig, axes = plt.subplots(ncols=4, nrows=1, figsize=(21, 5))
 
# Everything sarts with a Scatterplot
axes[0].set_title(player_name)
axes[0].plot(x, y, 'ko', alpha=0.9)
# As you can see there is a lot of overplottin here!
 
# Thus we can cut the plotting window in several hexbins
nbins = 100
axes[1].set_title(f'{player_name} hexes')
axes[1].hexbin(x, y, gridsize=nbins, cmap=my_cmap)
 
# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
k = kde.gaussian_kde(data.T)
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
 
# plot a density
axes[2].set_title(f'{player_name} gaussian')
axes[2].pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=my_cmap)
 
# add shading
axes[3].set_title(f'{player_name} density')
axes[3].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=my_cmap)


axes[0].imshow(img, extent=[-250, 250, -52, 418])
axes[1].imshow(img, extent=[-250, 250, -52, 418])
axes[2].imshow(img, extent=[-250, 250, -52, 418])
axes[3].imshow(img, extent=[-250, 250, -52, 418])

plt.show(fig)