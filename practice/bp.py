# import numpy as np
# import matplotlib.pyplot as plt

# x = ["C", "C++", "Java", "Python", "C#", "Bash"]
# y = [23, 17, 35, 29, 12, 41]

# plt.bar(x, y, color='purple', width=0.4, edgecolor='black')

# plt.title('Bar Plot')
# plt.xlabel('Programming Language')
# plt.ylabel('Popularity')

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'x': ['C', 'C++', 'Java', 'Python', 'C#', 'Bash'],
    'y': [23, 17, 35, 29, 12, 41]
}

df = pd.DataFrame(data)

# Plot using DataFrame
df.plot(
    x='x',
    y='y',
    kind='bar',
    color='purple',
    width=0.4,
    edgecolor='black',
    legend=False
)

# Add labels and title
plt.title('Bar Plot')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')

# Display the plot
plt.show()
 