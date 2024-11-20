import matplotlib.pyplot as plt
import seaborn as sns
from data import load_csv, explore_data

def visualize_data(df):
    """
    Present visualization options and create the selected visualization.
    """
    print("\nChoose a visualization type:")
    print("1: Line Plot")
    print("2: Bar Plot")
    print("3: Scatter Plot")
    print("4: Histogram")
    print("5: Correlation Heatmap")
    print("6: Sort Data")

    choice = input("Enter the number of the visualization type you want to create: ")

    if choice == '1':
        line_plot(df)
    elif choice == '2':
        bar_plot(df)
    elif choice == '3':
        scatter_plot(df)
    elif choice == '4':
        histogram(df)
    elif choice == '5':
        correlation_heatmap(df)
    elif choice == '6':
        sort(df)
    else:
        print("Invalid choice. Please select a valid visualization type.")

def line_plot(df):
    x_column = input("Enter the column for the x-axis: ")
    y_column = input("Enter the column for the y-axis: ")

    if x_column in df.columns and y_column in df.columns:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x=x_column, y=y_column)
        plt.title(f"Line Plot of {y_column} over {x_column}")
        plt.show()
    else:
        print("Invalid column names.")

def bar_plot(df):
    x_column = input("Enter the column for the x-axis: ")
    y_column = input("Enter the column for the y-axis: ")

    if x_column in df.columns and y_column in df.columns:
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x=x_column, y=y_column)
        plt.title(f"Bar Plot of {y_column} by {x_column}")
        plt.show()
    else:
        print("Invalid column names.")

def scatter_plot(df):
    x_column = input("Enter the column for the x-axis: ")
    y_column = input("Enter the column for the y-axis: ")

    if x_column in df.columns and y_column in df.columns:
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=df, x=x_column, y=y_column)
        plt.title(f"Scatter Plot of {y_column} vs {x_column}")
        plt.show()
    else:
        print("Invalid column names.")

def histogram(df):
    column = input("Enter the column for the histogram: ")

    if column in df.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(data=df, x=column, bins=30)
        plt.title(f"Histogram of {column}")
        plt.show()
    else:
        print("Invalid column name.")

def correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

def sort(df):
    column = input("Enter the column to sort by: ")
    if column in df.columns:
        asc = input("Type y for ascending or n for descending: ") == 'y'
        df_sorted = df.sort_values(by=column,  ascending = asc)
        print(df_sorted)
    else:
        print("Invalid column name.")

def run_visualizer():
    filepath = input("Enter the path to the CSV file: ")
    df = load_csv(filepath)
    
    if df is not None:
        explore_data(df)
        visualize_data(df)

# Run the visualizer
if __name__ == "__main__":
    run_visualizer()