import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size = 50)
y = np.random.normal(size = 50)
plt.scatter(x,y, color = 'red', alpha = 0.5)
plt.title("Random Dots")
plt.xlabel("X-axis")
plt.show()