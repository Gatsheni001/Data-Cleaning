import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv(r'C:\Users\giles\Desktop\Projects\employee_performance.csv')
print(df)

# Remove any duplicate rows from the DataFrame
df = df.drop_duplicates()
print("Dataframe after removing duplicates:")
print(df)

# Correct data types for all columns
# Remove non-numeric characters from Employee_ID
df['Employee_ID'] = df['Employee_ID'].str.extract('(\d+)').astype(float).astype('Int64')
df['Date'] = df['Date'].astype(str)
df['Hours_Worked'] = df['Hours_Worked'].fillna(0).astype(int)
df['Performance_Score'] = df['Performance_Score'].fillna(0).astype(int)
print("Dataframe after correcting data types:")
print(df)

#Transform the data to extract meaningful insights:
#Create a new column for the Year and Month extracted from the Date column.
df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Month'] = pd.to_datetime(df['Date']).dt.month
print("Dataframe after adding Year and Month columns:")
print(df)

#Calculate the average performance score for each department.
df['Department'] = df['Department'].str.lower()
avg_performance_score = df.groupby('Department')['Performance_Score'].mean()
print("Average performance score for each department:")
print(avg_performance_score)

#Identify the top 3 job roles with the highest average tasks completed per day.
df['Tasks_Completed_Per_Day'] = df['Tasks_Completed'] / df['Hours_Worked']
top_3_job_roles = df.groupby('Job_Role')['Tasks_Completed_Per_Day'].mean().nlargest(3)
print("Top 3 job roles with the highest average tasks completed per day:")
print(top_3_job_roles)


# Calculate the total tasks completed by employees in each department
total_tasks_completed = df.groupby('Department')['Tasks_Completed'].sum()
print("Total tasks completed by employees in each department:")
print(total_tasks_completed)

#Create a bar chart showing the average performance score for each department using plotly.

fig = px.bar(avg_performance_score, x=avg_performance_score.index, y='Performance_Score', title='Average Performance Score by Department')  
fig.show()
#Create a pie chart showing the proportion of total tasks completed by department.
fig = px.pie(total_tasks_completed, values='Tasks_Completed', names=total_tasks_completed.index, title='Proportion of Total Tasks Completed by Department')
fig.show()


# Create a line graph showing trends in the average tasks completed per hour across months
avg_tasks_completed_per_hour = df.groupby('Month')['Tasks_Completed_Per_Day'].mean().reset_index()


# Ensure all 12 months are included
all_months = pd.DataFrame({'Month': range(1, 13)})
avg_tasks_completed_per_hour = all_months.merge(avg_tasks_completed_per_hour, on='Month', how='left').fillna(0)

# Rename the columns for clarity
avg_tasks_completed_per_hour.columns = ['Month', 'Avg_Tasks_Completed_Per_Day']

# Create the line graph
fig = px.line(avg_tasks_completed_per_hour, x='Month', y='Avg_Tasks_Completed_Per_Day', title='Average Tasks Completed Per Day Across Months')
fig.update_layout(xaxis=dict(tickangle=-45))
fig.show()

#dentify which department shows the best overall performance and suggest ways to replicate their success in other departments
best_performing_department = avg_performance_score.idxmax()
print("Department with the best overall performance:", best_performing_department)

#Save the cleaned data to a new CSV file
df.to_csv(r'C:\Users\giles\Desktop\Projects\cleaned_employee_performance.csv', index=False)
print("Data saved to cleaned_employee_performance.csv")
