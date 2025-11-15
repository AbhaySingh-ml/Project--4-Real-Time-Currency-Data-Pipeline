# src/data_extractor.py

import requests
from src import config  # Import the configuration

def fetch_exchange_rates():
    """
    Fetches the latest exchange rates from the API.
    Returns the JSON response data as a Python dictionary.
    """
    print("Fetching data from API...")
    try:
        # Make the GET request using the URL from the config file
        response = requests.get(config.API_URL)
        
        # Raise an error for bad responses (like 404 or 500)
        response.raise_for_status()
        
        data = response.json()
        if data.get('result') == 'success':
            print("✅ Data fetched successfully!")
            return data
        else:
            # Handle API-specific errors (e.g., invalid key)
            print(f"❌ API Error: {data.get('error-type')}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., no internet)
        print(f"❌ Request Error: {e}")
        return None