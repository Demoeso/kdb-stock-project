import requests

API_KEY = "YOUR_API_KEY" 
symbol = "AAPL"
url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "outputsize": "compact",
    "datatype": "csv",
    "apikey": API_KEY
}

response = requests.get(url, params=params)

with open(f"{symbol}_daily.csv", "w") as f:
    f.write(response.text)

print(f"Downloaded {symbol}_daily.csv successfully.")

