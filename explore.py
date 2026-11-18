import pandas as pd

# EXERCISE 1: Load it
df = pd.read_csv('data/retail_sales.csv')

print("EXERCISE 1: Load it")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# EXERCISE 2: Filter by region
print("\nEXERCISE 2: Filter by region")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())


# EXERCISE 3: Top 5 by revenue
print("\nEXERCISE 3: Top 5 by revenue")

top5 = df.sort_values('revenue', ascending=False).head(5)

print(top5)


# EXERCISE 4: Two-condition filter
print("\nEXERCISE 4: Two-condition filter")

big_south = df[
    (df['region'] == 'South') & (df['revenue'] > 1000)
]

print(len(big_south))
print(big_south.head())


# EXERCISE 5: A new column
print("\nEXERCISE 5: A new column")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())


# EXERCISE 6: Unique values
print("\nEXERCISE 6: Unique values")

print(df['region'].unique())
print(df['region'].value_counts())


# EXERCISE 7: Select columns
print("\nEXERCISE 7: Select columns")

selected = df[['region', 'product', 'revenue']]

print(selected.shape)


# EXERCISE 8: Save
print("\nEXERCISE 8: Save")

df.to_csv('data/explored.csv', index=False)

print("File saved successfully!")
