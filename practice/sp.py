import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

plt.scatter(x_data, y_data, c='purple')

plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()