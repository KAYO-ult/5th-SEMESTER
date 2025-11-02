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
df = pd.DataFrame(data = {
    'programs': ['C', 'C++', 'Java', 'Python', 'C#', 'Bash'],
    'popularity': [23, 17, 35, 29, 12, 41],
    'meta': [55, 73, 94, 100, 20, 60]
})

# Plot using DataFrame
df.plot(
    x='programs',
    y= ['popularity', 'meta'],
    kind='bar',
    # color=['purple', 'orange'],
    width=0.4,
    edgecolor='white',
    legend=True
)

# Add labels and title
plt.title('Bar Plot')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')

# Display the plot
plt.show()
  