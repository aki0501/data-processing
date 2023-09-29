import pandas as pd

# Read csv file into a DataFrame
data = pd.read_csv('results.csv')

# Convert DataFrame to Excel
data.to_excel("results.xlsx", sheet_name="Sheet1")