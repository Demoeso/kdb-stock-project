from qpython import qconnection
import pandas as pd
import matplotlib.pyplot as plt

# Connect to q
with qconnection.QConnection(host='localhost', port=5000) as q:
    rec = q.sendSync('stockTable')

# Convert recarray to pandas DataFrame
stock = pd.DataFrame.from_records(rec)

# Convert kdb+ date (days since 2000-01-01) to datetime
stock['timestamp'] = pd.to_datetime('2000-01-01') + pd.to_timedelta(stock['timestamp'].astype(int), unit='D')

# Sort by timestamp
stock = stock.sort_values('timestamp')

# Plot
plt.figure(figsize=(12, 6))
plt.plot(stock['timestamp'], stock['close'], label='AAPL Close', color='blue')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("AAPL Closing Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
