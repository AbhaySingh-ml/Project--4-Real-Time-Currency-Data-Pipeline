# src/visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates # ## VERIFY THIS IMPORT IS PRESENT ##
import os

# Define the path for our data file and the output plot
DATA_FILE_PATH = "data/processed/exchange_rates.csv"
PLOT_FILE_PATH = "plots/exchange_rate_trends.png"

def generate_rate_plot():
    """
    Reads the stored exchange rate data and generates a time-series plot.
    """
    if not os.path.exists(DATA_FILE_PATH):
        print(f"Error: Data file not found at {DATA_FILE_PATH}")
        return

    print("Reading data and generating plot...")

    df = pd.read_csv(DATA_FILE_PATH)
    df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])
    df.set_index('timestamp_utc', inplace=True)
    
    columns_to_plot = [col for col in df.columns if col != 'base_currency']

    plt.style.use('ggplot') # Use the ggplot style for the plot
    fig, ax = plt.subplots(figsize=(12, 7))

    for currency in columns_to_plot:
        ax.plot(df.index, df[currency], label=currency, marker='o', linestyle='-')

    ax.set_title('USD Exchange Rate Trends Over Time', fontsize=16)
    ax.set_xlabel('Timestamp (UTC)')
    ax.set_ylabel('Exchange Rate (to 1 USD)')
    ax.legend()
    
    # ## THIS IS THE CRUCIAL FIX ##
    # Format the x-axis to show time clearly in Hour:Minute:Second
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    
    plt.xticks(rotation=45)
    plt.tight_layout()

    fig.savefig(PLOT_FILE_PATH)
    print(f"✅ Plot saved successfully to {PLOT_FILE_PATH}")
    
    plt.show()