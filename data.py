import pandas as pd

def load_csv(filepath):
    """
    Load CSV file into a DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print("The specified file was not found.")
        return None

def explore_data(df):
    """
    Print basic information about the dataset.
    """
    print("\nData Information:")
    print(df.info())
    print("\nFirst Five Rows:")
    print(df.head())
    print("\nStatistical Summary:")
    print(df.describe())
