import numpy as np
import matplotlib.pyplot as plt

years = [2005 + x for x in range(16)]
weight = [45, 55, 60, 62, 70, 72, 75, 78, 75, 82, 85, 87, 90, 92, 95, 88]

plt.plot(years, weight, c='purple', marker='o', linestyle='--')

plt.title('Line Plot')
plt.xlabel('Year')
plt.ylabel('Weight (kg)')

plt.show()  