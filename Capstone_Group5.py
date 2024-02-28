# capstone_group5.py

import pandas as pd
import numpy as np

# Function 1: Read Data
def read_data(file_path):
    """
    Read data from an Excel file and return a Pandas DataFrame.

    """
    data = pd.read_excel(file_path)
    return data

# Function 2: Data Preprocessing
def preprocess_data(data):
    """
    Perform basic preprocessing on the input data.
    """
    # Example: Fill missing values with the mean
    data.fillna(data.mean(), inplace=True)
    return data

# Function 3: Calculate Mean and Standard Deviation
def calculate_stats(data_column):
    """
    Calculate mean and standard deviation of a numeric column.

    """
    mean_value = np.mean(data_column)
    std_dev = np.std(data_column)
    return mean_value, std_dev

# Function 4: Generate Sample Data and Save to Excel
def generate_and_save_data(file_path):
    """
    Generate sample data and save it to an Excel file.

    """
    np.random.seed(42)
    data = pd.DataFrame({
        'numeric_column': np.random.rand(100),
        'other_column': np.random.randint(1, 100, 100),
    })

    data.to_excel(file_path, index=False)

# Main function for testing
def main():
    # Generate and save sample data to an Excel file
    generate_and_save_data(r'C:\Users\rdalal\Documents\ALY6000_RProject\datasets\Population.xlsx')

    # Read and process the data
    file_path = r'C:\Users\rdalal\Documents\ALY6000_RProject\datasets\Population.xlsx'
    data = read_data(file_path)
    preprocessed_data = preprocess_data(data)

    # Select a numeric column for statistical calculations
    numeric_column = preprocessed_data['numeric_column']

    # Calculate and print mean and standard deviation
    mean, std_dev = calculate_stats(numeric_column)
    print(f"Mean: {mean}, Standard Deviation: {std_dev}")

# Entry point for the script
if __name__ == "__main__":
    main()
