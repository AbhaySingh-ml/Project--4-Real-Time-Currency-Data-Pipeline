# src/pipeline.py

from src.data_extractor import fetch_exchange_rates
from src.data_transformer import transform_rate_data
from src.data_storage import save_to_csv
import time

def run_pipeline():
    """Defines the full sequence of operations for the data pipeline."""
    print(f"--- Pipeline run started at {time.ctime()} ---")

    # Phase 1: Fetch raw data
    raw_rate_data = fetch_exchange_rates()

    # Proceed only if data was fetched successfully
    if raw_rate_data:
        # Phase 2: Transform the raw data
        processed_data = transform_rate_data(raw_rate_data)

        # Phase 2: Store the processed data
        save_to_csv(processed_data)

    print("--- Pipeline run finished ---\n")