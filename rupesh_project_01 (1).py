# -*- coding: utf-8 -*-
"""Rupesh project-01

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16Hcs9a0CdtLktFiX3FGjGmtLGwuLPmO3
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = '/content/Airbnb NYC 2019.csv'
df = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
display(df.head())
print("\nDataset Info:")
df.info()
print("\nDataset Shape:", df.shape)
print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nSummary Statistics:")
display(df.describe())
print("\nRoom type distribution:")
print(df['room_type'].value_counts())
print("\nAverage price by neighbourhood group:")
print(df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False))
plt.figure(figsize=(10,6))
sns.histplot(df[df['price'] < 500]['price'], bins=50, kde=True)
plt.title('Price Distribution (Under $500)')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
df_clean = df.dropna()
print("Cleaned dataset shape:", df_clean.shape)

# Clean dataset if needed
df_clean = df.dropna()
print("Cleaned dataset shape:", df_clean.shape)