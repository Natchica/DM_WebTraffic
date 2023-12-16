import pandas as pd

# Basic Data Overview
def data_overview(df):
    nbRows = df.shape[0]
    nbColumns = df.shape[1]
    print("Data Shape:")
    print("\t- Number of rows:", nbRows)
    print("\t- Number of columns:", nbColumns)
    print("\nData Types:\n", df.dtypes[0:5])
    print("\nFirst Few Rows:\n", df.head())
    return nbRows, nbColumns

# Missing Values Analysis
def missing_values_analysis(df, rows, columns):
    missing_data = df.isnull().sum()
    columns_with_missing_values = missing_data[missing_data > 0].index.tolist()
    nbColumnsWmissingVal = len(columns_with_missing_values)
    print("\nPourcentage of columns with missing values:", round(nbColumnsWmissingVal/columns*100, 2), "% = ", nbColumnsWmissingVal, "/", columns, "=", columns-nbColumnsWmissingVal,"left if removed")
    rows_with_missing_values = df[df.isnull().any(axis=1)].index.tolist()
    nbRowsWmissingVal = len(rows_with_missing_values)
    print("Pourcentage of rows with missing values:", round(nbRowsWmissingVal/rows*100, 2), "% = ", nbRowsWmissingVal, "/", rows, "=", rows-nbRowsWmissingVal,"left if removed")

# Cleaning the data
def cleaning_data(df, rows, columns):
    df_cleaned = df.dropna()
    missing_data = df_cleaned.isnull().sum()
    print("Pourcentage of columns with missing values:", round(len(missing_data[missing_data > 0].index.tolist())/columns*100, 2), "%")
    print("Pourcentage of rows with missing values:", round(len(df_cleaned[df_cleaned.isnull().any(axis=1)].index.tolist())/rows*100, 2), "%")
    return df_cleaned


##### Main #####

# Load the data
file_path = 'web_traffic.csv'
df = pd.read_csv(file_path)

# Data Analysis
print("\n===== Data Analysis =====")
nbRows, nbColumns = data_overview(df)
missing_values_analysis(df, nbRows, nbColumns)
print("=========================")

# Data Cleaning
print("\n===== Cleaning the data =====")
df_cleaned = cleaning_data(df, nbRows, nbColumns)
print("=============================")

# Save the cleaned data
df_cleaned.to_csv('clean_web_traffic.csv', index=False)

# Cleaned Data Overview
print("\n===== Cleaned Data Overview =====")
_, _ = data_overview(df_cleaned)
print("=================================")
