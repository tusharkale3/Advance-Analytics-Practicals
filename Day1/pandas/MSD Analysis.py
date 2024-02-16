import pandas as pd 
import numpy as np 
import datetime 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("D:/CDAC/Advance Statistics/Day1/pandas/MS_Dhoni_ODI_record.csv")

# Basic checks
print(df.head())
print(df.tail())

# Data cleaning: Opposition name says 'v Aus', we can remove 'v '
df['opposition'] = df['opposition'].apply(lambda x: x[2:])

# Add a 'feature' - 'year' column using the match date column
# First convert date column into datetime format
df['date'] = pd.to_datetime(df['date'], dayfirst=True) 
df['year'] = df['date'].dt.year.astype(int)
#print(df.head())


# Create a column to distinguish between out and not out

# The apply method in Pandas allows you to apply a function to each element in a DataFrame or Series. In this case, the function being applied is str, which is the built-in Python function for converting values into strings. By applying str to each element in the 'score' column, we are converting the numerical or other data types in that column into string data types.
df['score'] = df['score'].apply(str) 
df['not_out'] = np.where(df['score'].str.endswith('*'), 1, 0)

# dropping the odi_number feature because it adds no value to the analysis
df.drop(columns='odi_number', inplace=True)

# dropping the odi_number feature because it adds no value to the analysis
df.drop(columns='odi_number', inplace=True)


