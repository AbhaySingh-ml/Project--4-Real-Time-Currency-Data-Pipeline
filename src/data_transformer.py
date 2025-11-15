# src/data_transformer.py

# from datetime import datetime

# def transform_rate_data(raw_data: dict) -> dict:
#     """
#     Transforms raw API data into a clean, flat dictionary.
#     """
#     print("Transforming raw data...")
    
#     # Extract the conversion rates dictionary
#     rates = raw_data.get("conversion_rates", {})
    
#     # Structure the data we want to keep
#     processed_data = {
#         "timestamp_utc": raw_data.get("time_last_update_utc"),
#         "base_currency": raw_data.get("base_code"),
#         "INR": rates.get("INR"),
#         "EUR": rates.get("EUR"),
#         "GBP": rates.get("GBP"),
#         "JPY": rates.get("JPY"), # Japanese Yen
#         "CAD": rates.get("CAD"), # Canadian Dollar
#         "AUD": rates.get("AUD")  # Australian Dollar
#     }
    
#     print("✅ Data transformed successfully!")
#     return processed_data

# src/data_transformer.py

from datetime import datetime, timezone

def transform_rate_data(raw_data: dict) -> dict:
    """
    Transforms raw API data into a clean, flat dictionary.
    """
    print("Transforming raw data...")
    
    # Extract the conversion rates dictionary
    rates = raw_data.get("conversion_rates", {})
    
    # --- THIS IS THE FIX ---
    # Get the current time in UTC, in a standard format.
    # This ensures each run has a unique timestamp.
    current_timestamp_utc = datetime.now(timezone.utc).isoformat()
    
    # Structure the data we want to keep
    processed_data = {
        "timestamp_utc": current_timestamp_utc, # Use our new timestamp
        "base_currency": raw_data.get("base_code"),
        "INR": rates.get("INR"),
        "EUR": rates.get("EUR"),
        "GBP": rates.get("GBP"),
        "JPY": rates.get("JPY"),
        "CAD": rates.get("CAD"),
        "AUD": rates.get("AUD")
    }
    
    print("✅ Data transformed successfully!")
    return processed_data