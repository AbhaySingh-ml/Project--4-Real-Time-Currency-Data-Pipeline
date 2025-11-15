# # main.py

# import json
# from src.data_extractor import fetch_exchange_rates

# if __name__ == "__main__":
#     print("--- Starting Currency Data Pipeline ---")
    
#     # Call the function to get the data
#     rate_data = fetch_exchange_rates()
    
#     # If data was fetched successfully, print it
#     if rate_data:
#         print("\n--- Sample of Fetched Data ---")
#         # Pretty-print the JSON data to the console
#         print(json.dumps(rate_data, indent=4))
        
#     print("\n--- Pipeline Run Finished ---")

# main.py

# from src.data_extractor import fetch_exchange_rates
# from src.data_transformer import transform_rate_data
# from src.data_storage import save_to_csv

# if __name__ == "__main__":
#     print("--- Starting Currency Data Pipeline ---")
    
#     # Phase 1: Fetch raw data
#     raw_rate_data = fetch_exchange_rates()
    
#     # Proceed only if data was fetched successfully
#     if raw_rate_data:
#         # Phase 2: Transform the raw data
#         processed_data = transform_rate_data(raw_rate_data)
        
#         # Phase 2: Store the processed data
#         save_to_csv(processed_data)
        
#     print("\n--- Pipeline Run Finished ---")

# main.py

import schedule
import time
from src.pipeline import run_pipeline

if __name__ == "__main__":
    print("🚀 Starting the automated data pipeline scheduler.")

    # Schedule the pipeline to run every 1 minute.
    # You can change this to .minutes, .hour, .day.at("10:30") etc.
    schedule.every(1).minutes.do(run_pipeline)

    # Run the pipeline once immediately at the start
    run_pipeline()

    # Loop forever so the scheduler can run
    while True:
        schedule.run_pending()
        time.sleep(1)