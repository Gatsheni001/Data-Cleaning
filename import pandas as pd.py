import pandas as pd
 
# Create the main CSV file
data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'computer_id': [175437, 2238623, 3468732, 4432489, 5983724],
    'device_name': [
        'CAPACITI-JHB 2293',
        'CAPACITI-JHB 2263',
        'CAPACITI-JHB 2223',
        'CAPACITI-JHB 2278',
        'CAPACITI-JHB 2209'
    ],
    'session_id': [
        'abc123xyz', 'ghi589xyz', 'lmn987xyz', 'def435xyz', 'opq461xyz'
    ]
})
data.to_csv('data.csv', index=False)
 
# Create the JSON file
json_data = [
    {"department_id": 101, "department_name": "Data Engineering"},
    {"department_id": 102, "department_name": "Data Engineering"},
    {"department_id": 103, "department_name": "Data Engineering"},
    {"department_id": 104, "department_name": "Data Engineering"},
    {"department_id": 105, "department_name": "Data Engineering"}
]
pd.DataFrame(json_data).to_json('data.json', orient='records', lines=True)
 
# Read the main files
csv_data = pd.read_csv('data.csv')
json_data = pd.read_json('data.json', lines=True)
 
# Merge all data
merged_data = pd.concat([csv_data, json_data], axis=1)
 
# Resolve conflicts and ensure data consistency
merged_data.fillna({
    'device_name': 'Unknown',
    'session_id': 'Unknown',
    'department_name': 'Unknown'
}, inplace=True)
 
# Drop redundant columns
if 'name_y' in merged_data.columns:
    merged_data.drop(columns=['name_y'], inplace=True)
 
# Save the merged data to a new CSV file
merged_data.to_csv('merged_data.csv', index=False)
 
# Display the merged data on the terminal
print("Merged Data:")
print(merged_data)
 