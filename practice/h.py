import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5, 1, 10)
print(x)
plt.hist(x)
plt.title('Histogram')
# plt.xlabel('Value') 
# plt.ylabel('Frequency')
plt.show()