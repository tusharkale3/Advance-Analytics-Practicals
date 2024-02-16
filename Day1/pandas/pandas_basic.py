import pandas as pd
df = pd.read_csv("Dummy_Sales_Data_v1.csv")

# Getting dataset overview
print(df) # prints the entire DataFrame, which will display all the rows and columns of the loaded CSV data.
print(df.head()) #  prints the first 5 rows (by default) of the DataFrame
print(df.tail()) # prints the last 5 rows (by default) of the DataFrame
print(df.sample()) # prints a random row from the DataFrame 
print(df.info()) # prints a concise summary of the DataFrame's information. It includes details such as the number of non-null entries in each column, data types, and memory usage.
print(df.describe()) # prints basic statistics for the numeric columns in the DataFrame
print(df.nunique()) # used to count the number of unique values in each column of a pandas DataFrame. When you call df.nunique(), it returns a Series where the index is the column names, and the values are the counts of unique values in each respective column.

# Force to display everything
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print(df)

# Reset
pd.reset_option("display.max_rows")
pd.reset_option("display.max_columns")


# Selecting a subset
print(df.query("Quantity > 95"))

# Get the value at the intersection of the 100th row and the 'Sales_Manager' column
print(df.loc[100,'Sales_Manager'])

# Return a subset of the original DataFrame df containing rows 100 and 200 and columns 6 and 3. We will get a DataFrame that includes data from these specific rows and columns based on their integer positions.
print(df.iloc[[100, 200],[6,3]])

# loc – select by labels
# iloc – select by positions

# Deeper analysis
print(df["Sales_Manager"].unique())	# Values
print(df["Sales_Manager"].nunique()) # Count
print(df.nunique())	# For all columns
print(df.isnull())	# True/false for each column
