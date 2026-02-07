import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

EXPENSE_FILE = 'expenses.csv'
SUMMARY_FILE = 'monthly_summary.csv'
PLOT_FILE = 'spending_plot.png'

CATEGORIES = ['Food', 'Rent', 'Transport', 'Entertainment', 'Utilities', 'Shopping']

def generate_sample_data(filename=EXPENSE_FILE, num_records=50):
    """Generates a CSV file with random expense data if it doesn't exist."""
    if os.path.exists(filename):
        print(f"'{filename}' already exists. Skipping generation.")
        return

    print(f"Generating sample data in '{filename}'...")
    data = []
    start_date = datetime.now() - timedelta(days=90) # Last 3 months

    for _ in range(num_records):
        date = start_date + timedelta(days=random.randint(0, 90))
        category = random.choice(CATEGORIES)
        description = f"Sample {category} expense"
        # Random amount between 100 and 5000 Rs
        amount = round(random.uniform(100, 5000), 2)
        data.append([date.strftime('%Y-%m-%d'), category, description, amount])

    df = pd.DataFrame(data, columns=['Date', 'Category', 'Description', 'Amount (Rs)'])
    df.to_csv(filename, index=False)
    print("Data generation complete.")

def load_data(filename=EXPENSE_FILE):
    """Loads expense data from CSV."""
    try:
        df = pd.read_csv(filename)
        print(f"Loaded {len(df)} records from '{filename}'.")
        return df
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return None

# Monthly Budget Thresholds (Rs)
THRESHOLDS = {
    'Food': 10000,
    'Rent': 20000,
    'Transport': 5000,
    'Entertainment': 5000,
    'Utilities': 5000,
    'Shopping': 8000
}

def process_data(df):
    """Groups data by Month and Category, sums amounts, and flags overspending."""
    # Ensure Date is datetime
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    summary = df.groupby(['Month', 'Category'])['Amount (Rs)'].sum().reset_index()
    
    # Flag overspending
    summary['Over Budget'] = summary.apply(
        lambda row: 'Yes' if row['Amount (Rs)'] > THRESHOLDS.get(row['Category'], 999999) else 'No',
        axis=1
    )
    
    return summary

def save_summary(df, filename=SUMMARY_FILE):
    df.to_csv(filename, index=False)
    print(f"Summary saved to '{filename}'.")

def plot_data(summary, filename=PLOT_FILE):
    """Plots spending by category per month."""
    # Pivot for plotting: Month vs Category
    pivot_df = summary.pivot(index='Month', columns='Category', values='Amount (Rs)')
    
    # Plot
    ax = pivot_df.plot(kind='bar', figsize=(10, 6), rot=0)
    plt.title('Monthly Spending by Category')
    plt.ylabel('Amount (Rs)')
    plt.xlabel('Month')
    plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    # Save
    plt.savefig(filename)
    print(f"Plot saved to '{filename}'.")
    plt.close()

def main():
    generate_sample_data()
    df = load_data()
    if df is not None:
        print("Data Sample:")
        print(df.head())
        
        summary = process_data(df)
        print("\nMonthly Summary:")
        print(summary)
        
        save_summary(summary)
        plot_data(summary)

if __name__ == "__main__":
    main()
