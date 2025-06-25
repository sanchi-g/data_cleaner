import pandas as pd

input_file="dirty_data.csv"
output_file="cleaned_data.csv"

df = pd.read_csv(input_file)

print("Before cleaning:")
print(df.info())
print(df)

# Drop rows with any nulls in units column
df_clean = df.dropna(subset=['Name','Units'])
df_clean = df_clean.fillna('')

#alternate method
'''for x in df_clean.index:
        if (df_clean.loc[x, "Units"]=='' or df_clean.loc[x, "Name"]==''):
            df_clean.drop(x, inplace=True)'''
    
# Convert all columns to string (example type conversion)
df_clean[df_clean.columns] = df_clean[df_clean.columns].astype(str)

# sort data by name
df_clean=df_clean.sort_values(by='Name')

# to add new index
df_clean = df_clean.reset_index(drop=True)
    
print("\nAfter cleaning:")
print(df_clean.info())
print(df_clean)

df_clean.to_csv(output_file)
print("Cleaned data saved to",output_file,".")

