import pandas as pd

# Step 1: Read the list of websites from the Parquet file
parquet_file_path = r"C:\Proiecte JS\Challange\list of company websites.snappy.parquet"  # Use a raw string for Windows paths
data = pd.read_parquet(parquet_file_path)

# Step 2: Inspect the DataFrame
print(data.head())  # Print the first few rows of the DataFrame to see the structure
print(data.columns)  # Print the column names to identify the correct column
