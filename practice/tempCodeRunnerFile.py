import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create dataframe
df = pd.DataFrame(data={
    'index': np.arange(30),
    'a':np.random.randint(0,100,30),
    'b':np.random.randint(0,100,30),
    'c':np.random.randint(0,100,30)
})

# (a) figure 15x8 with two subplots
# fig, (ax1, ax2) = plt.subplots(2,1, figsize=(15,8))

plt.subplot(2,2,1)
df.plot(y=['b','a'], kind='line', ax=plt.gca())

# plt.plot(df['a'], color='green', label='Green')
# plt.plot(df['b'], color='orange', label='Orange')

plt.subplot(2,2,2)
df.plot(x='a', y='c', kind='scatter', ax=plt.gca())

# plt.scatter(df.index, df['c'], marker='o')

# top subplot: two lines: a = green, b = orange
# ax1.plot(df['a'], color='green', label='Green')
# ax1.plot(df['b'], color='orange', label='Orange')
# ax1.legend(loc='upper center')

# bottom subplot: only data points (circles) no connecting line -> scatter
# ax2.scatter(df.index, df['c'], marker='o')


# (b) bar graph for full dataframe
# df.plot(kind='bar', figsize=(10,5))
plt.subplot(2,2,3)
df.plot(x='index', y=['a','b','c'], kind='bar', ax=plt.gca())

plt.tight_layout()
plt.show()