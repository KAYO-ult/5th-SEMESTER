import numpy as np
import matplotlib.pyplot as plt

programming_languages = ["C", "C++", "Java", "Python", "C#", "Bash"]
popularity = [23, 17, 35, 29, 12, 41]

plt.pie(popularity, labels=programming_languages, autopct='%.2f%%')
plt.title('Pie Chart')
plt.show() 


