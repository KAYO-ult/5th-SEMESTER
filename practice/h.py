import matplotlib.pyplot as plt
import numpy as np

# x = [12, 15, 14, 10, 18, 20, 25, 30, 22, 19, 24, 28, 35, 40, 38, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
x = np.random.randint(0, 100, 50)
print(x)
plt.hist(x)
plt.title('Histogram')
# plt.xlabel('Value') 
# plt.ylabel('Frequency')
plt.show()