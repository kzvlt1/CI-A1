import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2)
lines = plt.plot(t, t, 'b-', t, t**3, 'g-', linewidth=2.0)
plt.setp(lines, color = 'r', linewidth = 2.0)
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()  