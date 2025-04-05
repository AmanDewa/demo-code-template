import pandas as pd

# Sample employee information dataset
data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT"],
    "Salary": [60000, 75000, 50000, 65000, 70000],
    "JoiningDate": ["2020-01-15", "2019-03-10", "2021-07-01", "2018-11-20", "2020-06-25"]
}

# Create a pandas DataFrame
employee_df = pd.DataFrame(data)

# Convert JoiningDate to datetime format
employee_df["JoiningDate"] = pd.to_datetime(employee_df["JoiningDate"])

# Display the DataFrame


print(employee_df)
employee_df.head() 
