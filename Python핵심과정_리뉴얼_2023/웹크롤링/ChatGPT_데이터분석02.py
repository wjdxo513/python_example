import pandas as pd
import numpy as np

# Generate random product data
np.random.seed(123)
n = 100
product_id = np.arange(1, n+1)
product_name = ['Product ' + str(i) for i in product_id]
product_price = np.random.randint(100, 1000, n)
category_id = np.random.randint(1, 4, n)

# Create a dictionary from the data
data = {'Product ID': product_id,
        'Product Name': product_name,
        'Product Price': product_price,
        'Category ID': category_id}

# Convert the dictionary to a DataFrame and write to CSV file
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Calculate the sum and average price of the products
total_price = df['Product Price'].sum()
avg_price = df['Product Price'].mean()

# Print the results
print(f"Total price of all products: {total_price}")
print(f"Average price of all products: {avg_price:.2f}")