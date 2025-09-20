import numpy as np
import matplotlib.pyplot as plt

x = ["C", "C++", "Java", "Python", "C#", "Bash"]
y = [23, 17, 35, 29, 12, 41]

plt.bar(x, y, color='purple', width=0.4, edgecolor='black')

plt.title('Bar Plot')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')

plt.show()
