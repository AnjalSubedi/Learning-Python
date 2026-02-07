# Expense Tracker 💰

A simple yet practical Python script to track expenses, analyze monthly spending, and visualize budget adherence.

## Features

- **Automated Data Generation**: Generates sample expense data if none exists.
- **Categorization**: Groups expenses by category (Food, Rent, Transport, etc.).
- **Budget Monitoring**: Flags categories that exceed defined monthly budgets (in Rs).
- **Visualization**: Generates a bar chart showing monthly spending by category.
- **CSV Reports**: Exports a detailed monthly summary to CSV.

## Prerequisites

- Python 3.x
- pandas
- matplotlib

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/AnjalSubedi/Learning-Python.git
    cd Learning-Python
    ```
    *(Note: Adjust directory if you cloned into `expense_tracker` specifically)*

2.  Install dependencies:
    ```bash
    pip install pandas matplotlib
    ```

## Usage

Run the script:

```bash
python expense_tracker.py
```

## Output

The script will generate:
- `expenses.csv`: Raw expense data.
- `monthly_summary.csv`: Aggregated data with "Over Budget" flags.
- `spending_plot.png`: A bar chart visualizing the data.

### Example Console Output
```
Monthly Summary:
     Month       Category  Amount (Rs) Over Budget
0  2025-11           Food      3962.61          No
1  2025-11           Rent      9241.92          No
2  2025-11       Shopping      8502.58         Yes
...
```
