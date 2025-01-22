import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
import pandas as pd

# Assuming df is your DataFrame
# Convert columns to numeric, forcing errors to NaN
df = df.apply(pd.to_numeric, errors='coerce')

# Fill missing values with the mean of the column
df_filled_mean = df.fillna(df.mean())
print("DataFrame after filling missing values with mean:")
print(df_filled_mean)
print()

# Fill missing values with the median of the column
df_filled_median = df.fillna(df.median())
print("DataFrame after filling missing values with median:")
print(df_filled_median)
print()

# Fill missing values with the mode of the column
df_filled_mode = df.fillna(df.mode().iloc[0])
print("DataFrame after filling missing values with mode:")
print(df_filled_mode)
print()

#provide the updated data
print("Updated Data:")
print(df)

df_cleaned = df.drop_duplicates()
print("DataFrame after removing duplicates:")
print(df_cleaned)
print()

print()
# Dataset with standardized column names.
df_standardized = df.rename(columns={'CustomerID': 'customer_id', 'TransactionDate': 'Transaction_Date', 'TransactionAmount': 'Transaction_Amount'})
print("DataFrame with standardized column names:")
print(df_standardized.columns)  
print()

# Verify the column names
print("Columns in df_standardized:", df_standardized.columns)
print()

# Correct data types
def correct_data_types(df):
    date_columns = df.select_dtypes(include=['object']).columns
    for col in date_columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass
    return df

df_corrected = correct_data_types(df_standardized)
print("DataFrame with corrected data types:")
print(df_corrected)

#Use boxplots to detect outliers in numerical columns.
df_corrected.boxplot(column=['Transaction_Amount'])
plt.title('Boxplot of Transaction Amount')
plt.show()

# Remove outliers using the IQR method.
Q1 = df_corrected['Transaction_Amount'].quantile(0.25)
Q3 = df_corrected['Transaction_Amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_corrected = df_corrected[(df_corrected['Transaction_Amount'] >= lower_bound) & (df_corrected['Transaction_Amount'] <= upper_bound)]
print("DataFrame after removing outliers:")
print(df_corrected)
print()




