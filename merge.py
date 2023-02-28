import pandas as pd

# Read the first CSV file into a pandas dataframe
df1 = pd.read_csv('bright_star.csv')

# Read the second CSV file into a pandas dataframe
df2 = pd.read_csv('brown_dwarfs.csv')

# Merge the two dataframes based on a common column
merged_df = pd.merge(df1, df2, on='common_column')

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged_file.csv', index=True)