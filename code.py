import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/dell/Desktop/Solar power/dataset.csv')
df.head()
df.tail()
df.shape
df.describe()
df.info()
df.isnull().sum()
df.duplicated().sum()
plt.figure(figsize=(10,8))
sns.histplot(df['generated_power_kw'],bins=30,kde=True)
plt.title('Solar power consumed(kW)')
plt.xlabel('generated_power_kw')
plt.ylabel('Frequency')
plt.show()
