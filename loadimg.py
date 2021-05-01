import matplotlib.pyplot as plt
img = plt.imread("test.png")
fig, ax = plt.subplots()
x = range(300)
ax.imshow(img, extent=[0, 400, 0, 300])
ax.plot(x, x, '--', linewidth=5, color='firebrick')

plt.show(fig)