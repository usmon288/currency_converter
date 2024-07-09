import requests

def get_exchange_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        raise Exception("Failed to fetch exchange rates")

def convert_currency(amount: float, rates: dict) -> dict:
    conversions = {currency: amount * rate for currency, rate in rates.items()}
    return conversions
