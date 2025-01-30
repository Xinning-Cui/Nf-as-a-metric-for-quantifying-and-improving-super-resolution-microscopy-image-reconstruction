import pandas as pd

# Load the Excel file
file_path = r"path to\VanillaCVDM_all_metrics.xlsx"  # Replace with your file path 
df = pd.read_excel(file_path, header=None)  

# Set the first row as column headers
df.columns = df.iloc[0]  
df = df[1:]  # Remove the first row from the data

# # Debugging: Check the processed data
# print("\nProcessed DataFrame:")
# print(df.head())

# Calculate the Pearson correlation coefficient matrix
correlation_matrix = df.corr(method='pearson').round(3)

# Display the correlation matrix
print("\nPearson Correlation Coefficient Matrix:")
print(correlation_matrix)

# Optionally, save the correlation matrix to a CSV file
#correlation_matrix.to_csv(r"path to\VanillaCVDM_correlation_matrix.csv", index=True)
