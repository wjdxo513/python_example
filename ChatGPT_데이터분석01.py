import pandas as pd

# Create a dictionary of data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Print the data types of each column
print(df.dtypes)

# Print the mean age of the people in the DataFrame
print(df['Age'].mean())
