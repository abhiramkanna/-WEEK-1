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
df[df.columns[0:9]].hist(bins=30,figsize=(20,20))
plt.show()
df[df.columns[9:18]].hist(bins=30,figsize=(20,20))
plt.show()
df[df.columns[18:21]].hist(bins=30,figsize=(20,20))
plt.show()
#bivariate
#scatterplot
plt.figure(figsize=(15,20))
for i, column in enumerate(df.columns):
    plt.subplot(7,3,i+1)
    plt.scatter(df[column],df['generated_power_kw'])
    plt.title(f'{column} vs Genrate power(Kw)')
    plt.xlabel(column)
    plt.ylabel('generated_power_kw')
plt.tight_layout()
plt.show()
df.corr()
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(),cmap='coolwarm',annot=True,fmt='.2f')
#outlier
plt.figure(figsize=(15,30))
for i, column in enumerate(df.columns):
    plt.subplot(7,3,i+1)
    sns.boxplot(df[column])
