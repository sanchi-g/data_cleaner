# data_cleaner
A Python-based data cleaning utility that reads CSV files, removes missing values, standardizes data types, sorts entries, and exports cleaned output. Built using Pandas for preprocessing automation.

Data Cleaner Script

This is a simple Python script to clean and preprocess tabular CSV data. It removes missing entries in key columns, standardizes data types, sorts entries, resets indexing, and exports a cleaned version of the dataset.

Features

- Removes rows where `Name` or `Units` is missing
- Converts all column values to strings for consistency
- Sorts data alphabetically by `Name`
- Resets row index and saves cleaned output to a new CSV

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



Author

**Sanchi Goyal**  
Final-year B.Tech | Data • DevOps • Python  
GitHub: [github.com/sanchi-g](https://github.com/sanchi-g)
