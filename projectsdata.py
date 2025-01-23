import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('customer_transactions.csv')

# Display the first 10 rows
print(df.head(10))

# Summarize its structure
print(df.info())

# Identify columns with missing values and their percentage
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
print("Missing values and their percentage:")
print(missing_percentage)

# Drop rows with missing values
df_dropped = df.dropna()
print("DataFrame after dropping missing values:")
print(df_dropped)


# Verify the column names
print("Columns in df_dropped:", df_dropped.columns)
print()

#Remove duplicate rows
Remove_duplicate = df_dropped.drop_duplicates()
print("DataFrame after removing duplicates:")
print(Remove_duplicate)

# Standardize the format of the string data
df_dropped['customer_id'] = df_dropped['customer_id'].astype(str).str.Upper()                                
df_dropped['state'] = df_dropped['state'].str.upper()
print("DataFrame after standardizing customer IDs and state names:")
print(df_dropped[['customer_id', 'state']])

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

df_corrected = correct_data_types(df_dropped)
print("DataFrame with corrected data types:")
print(df_corrected)

# Use boxplots to detect outliers in numerical columns
plt.figure(figsize=(10, 6))
df_corrected.boxplot(column=['Transaction_Amount'])
plt.title('Boxplot of Transaction Amount')
plt.xticks(rotation=45)
plt.show()

# Remove outliers using the IQR method
Q1 = df_corrected['Transaction_Amount'].quantile(0.25)
Q3 = df_corrected['Transaction_Amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_corrected = df_corrected[(df_corrected['Transaction_Amount'] >= lower_bound) & (df_corrected['Transaction_Amount'] <= upper_bound)]
print("DataFrame after removing outliers:")
print(df_corrected)

#Standardize the format of the string data.
df_corrected['customer_id'] = df_corrected['customer_id'].astype(str).str.upper()
df_corrected['state'] = df_corrected['state'].str.upper()
print("DataFrame after standardizing customer IDs and state names:")
print(df_corrected[['customer_id', 'state']])
print()

#Remove irrelevant columns from the dataset.
df_corrected = df_corrected.drop(['customer_id','state'], axis=1)
print("Data with irrelevent columns removed:")
print(df_corrected)
print() 

# Visualizations
plt.figure(figsize=(12, 6))
plt.bar(missing_percentage.index, missing_percentage.values)
plt.xlabel('Columns')
plt.ylabel('Percentage of Missing Values')
plt.title('Missing Values')
plt.xticks(rotation=45)
plt.show()



# Create a new CSV file with the cleaned and standardized data
df_corrected.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved to 'cleaned_data.csv'")