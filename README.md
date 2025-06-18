# Stock Visualizer

This project fetches Apple's daily stock data using Alpha Vantage, loads it into a kdb+ database using a Q script, and visualizes the closing prices using Python and Matplotlib.

## Files:
- `Fetch_Stocks.py`: Downloads daily stock data from Alpha Vantage.
- `AAPL_daily.csv`: The downloaded data.
- `Load_CSV.q`: Loads the CSV into a kdb+ table called `stockTable`.
- `Plot_Stock.py`: Connects to kdb+ and plots the closing prices.
