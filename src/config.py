# src/config.py

# Your actual API key from exchangerate-api.com
API_KEY = '7608ef4c0af4b323f0ea2943'

# The base currency for which you want to get exchange rates
BASE_CURRENCY = 'USD'

# Construct the complete API URL
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"