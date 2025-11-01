
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data={
    'months': [1,2,3,4,5,6,7,8,9,10,11,12],
    'anudeep': np.random.randint(2000,50000,12),
    'aneek': np.random.randint(1000,30000,12),
    'souporno':  np.random.randint(3000,60000,12),
    'arya': np.random.randint(1500,45000,12)    
}

df = pd.DataFrame(data)

plt.subplot(2, 2, 1)
df.plot(x='months', y='anudeep', kind='line', marker='o', color='blue', label='Anudeep', ax=plt.gca())
plt.title('Anudeep Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Units')

plt.subplot(2, 2, 2)
df.plot(x='months', y='aneek', kind='line', marker='o', color='green', label='Aneek', ax=plt.gca())
plt.title('Aneek Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Units')

plt.subplot(2, 2, 3)
df.plot(x='months', y='souporno', kind='line', marker='o', color='red', label='Souporno', ax=plt.gca())
plt.title('Souporno Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Units')

plt.subplot(2, 2, 4)
df.plot(x='months', y='arya', kind='line', marker='o', color='purple', label='Arya', ax=plt.gca())
plt.title('Arya Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Units')

plt.tight_layout()
plt.show()