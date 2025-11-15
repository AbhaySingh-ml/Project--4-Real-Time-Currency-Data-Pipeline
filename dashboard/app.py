# dashboard/app.py

import streamlit as st
import pandas as pd
import os

# Path to your CSV file
DATA_FILE_PATH = "data/processed/exchange_rates.csv"

@st.cache_data(ttl=60)
def load_data():
    """
    Loads data from the CSV file.
    Uses Streamlit's cache to reload data every 60 seconds.
    """
    if not os.path.exists(DATA_FILE_PATH):
        # If file doesn't exist, return an empty DataFrame
        return pd.DataFrame() 
    
    df = pd.read_csv(DATA_FILE_PATH)
    # Convert timestamp to datetime and set it as the index
    df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])
    df.set_index('timestamp_utc', inplace=True)
    return df

# --- Page Configuration ---
# Set the page to be wide
st.set_page_config(
    page_title="Currency Exchange Dashboard",
    layout="wide"
)

# --- Title ---
st.title("Live Currency Exchange Rate Dashboard")

# --- Load Data ---
df = load_data()

# --- Display Data ---
if df.empty:
    st.warning("No data found. Please run the data collector script: python main.py")
else:
    st.success(f"Data loaded successfully! Last update: {df.index.max()}")

    # --- Display the Line Chart ---
    st.subheader("Currency Trends Over Time")
    
    # Get all columns except 'base_currency' to plot
    columns_to_plot = [col for col in df.columns if col != 'base_currency']
    
    # Use Streamlit's built-in line chart
    st.line_chart(df[columns_to_plot])

    # --- Display the Raw Data Table ---
    st.subheader("Raw Data Log")
    # Display the full DataFrame in an interactive table
    st.dataframe(df)