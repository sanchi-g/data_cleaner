# data_cleaner
A Python-based data cleaning utility that reads CSV files, removes missing values, standardizes data types, sorts entries, and exports cleaned output. Built using Pandas for preprocessing automation.

---

Features

- Removes rows where `Name` or `Units` is missing
- Converts all column values to strings for consistency
- Sorts data alphabetically by `Name`
- Resets row index and saves cleaned output to a new CSV

---

Input Format

A CSV file named `dirty_data.csv` with at least the following columns:

```
Name,Units,Date,...
```

Example:
```csv
Name,Units,Date
Riya,12,2024-01-01
,10,2024-01-02
Aman,,2024-01-03
```

How to Run

1. Place your `dirty_data.csv` file in the same directory.
2. Run the script:
```bash
python data_cleaner.py
```

The cleaned file will be saved as `cleaned_data.csv`.

Requirements

- Python 3.x
- pandas

 Output Example
```
After cleaning:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    10 non-null     object
 1   Units   10 non-null     object
 2   Date    10 non-null     object
dtypes: object(3)
memory usage: 372.0+ bytes
None
      Name  Units       Date
0  Plant A  100.0   1/1/2024
1  Plant D  150.0   1/4/2024
2  Plant E  246.0  1/12/2024
3  Plant F  143.0   1/6/2024
4  Plant G  164.0   1/7/2024
5  Plant I  167.0  1/13/2024
6  Plant K  186.0           
7  Plant N  135.0  1/11/2024
8  Plant P  157.0  1/15/2024
9  Plant Q  165.0  1/16/2024
Cleaned data saved to cleaned_data.csv .
```
Author

**Sanchi Goyal**  
Final-year B.Tech | Data • DevOps • Python  
GitHub: [github.com/sanchi-g](https://github.com/sanchi-g)
