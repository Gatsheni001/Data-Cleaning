import pandas as pd
import numpy as np


#I want to read a CSV file and open it to clean the data
df = pd.read_csv('customer_transactions.csv')
# i want to see .head(10)
print(df.head(10))

#Summarize it structure
print(df.info())

#Identify columns with missing values and their percentage.
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
print("Missing values and their percentage:")
print(missing_percentage)

# Dropping missing values
df_dropped = df.dropna()
print("DataFrame after dropping missing values:")
print(df_dropped)
print()





'''
# Performing k-means clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(df_imputed[['Age', 'Salary']])
# Get cluster labels for the data points
clusters = kmeans.labels_
print("Cluster labels:")
print(clusters)'''