import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2)
lines = plt.plot(t, t, 'r-', t, t**3, 'g-', linewidth = 2.0)
plt.setp(lines, color = 'r', linewidth = 2.0)
plt.xlabel('Dumma data for x')
plt.ylabel('Dummy data for y')
plt.title('An example graph')
plt.annotate('Divergence point', xy = (1.4, 3), xytext = (3, 1.5), arrowprops = dict(facecolor = 'black', shrink = 0.05))
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()