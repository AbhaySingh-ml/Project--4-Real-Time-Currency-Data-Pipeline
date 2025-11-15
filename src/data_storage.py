# src/data_storage.py

import pandas as pd
import os

# Define the path for our output CSV file
FILE_PATH = "data/processed/exchange_rates.csv"

def save_to_csv(processed_data: dict):
    """
    Saves a dictionary of processed data to a CSV file.
    Appends the data as a new row if the file already exists.
    """
    print(f"Saving data to {FILE_PATH}...")
    
    # Convert our single dictionary into a pandas DataFrame
    # The [0] is needed to wrap the dictionary in a list, creating a single-row DataFrame
    df = pd.DataFrame([processed_data])
    
    # Check if the CSV file already exists
    file_exists = os.path.exists(FILE_PATH)
    
    # If the file exists, append without the header.
    # Otherwise, create the file and write the header.
    df.to_csv(
        FILE_PATH, 
        mode='a',             # 'a' stands for append
        header=not file_exists, # Write header only if file does not exist
        index=False           # Don't write the DataFrame index
    )
    
    print("✅ Data saved successfully!")

# src/data_storage.py

# import pandas as pd
# import os

# # Define the path for our output CSV file
# FILE_PATH = "data/processed/exchange_rates.csv"

# def save_to_csv(processed_data: dict):
#     """
#     Saves a dictionary of processed data to a CSV file.
#     Appends the data as a new row if the file already exists.
#     """
#     print(f"Saving data to {FILE_PATH}...")
    
#     # Convert our single dictionary into a pandas DataFrame
#     df = pd.DataFrame([processed_data])
    
#     # Check if the CSV file already exists
#     file_exists = os.path.exists(FILE_PATH)
    
#     # --- THIS IS THE FIX ---
#     # We must use mode='a' (for append)
#     # We also check if the file exists, so we only write the header once.
#     df.to_csv(
#         FILE_PATH, 
#         mode='a',             # 'a' stands for append
#         header=not file_exists, # Write header only if file does NOT exist
#         index=False           # Don't write the DataFrame index
#     )
    
#     print("✅ Data saved successfully!")