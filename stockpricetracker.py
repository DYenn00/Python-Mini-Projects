//stock price tracker 

!pip install yfinance
import yfinance as yf
import time
import os

def get_stock_price(ticker):
    """Fetch the latest stock price for a given ticker."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return price
    except Exception as e:
        print("Error fetching price:", e)
        return None

def track_stock(ticker, interval=10):
    """Continuously track a stock's price at specified intervals."""
    print(f"Tracking live prices for {ticker}...\n(Press Ctrl+C to stop)\n")
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}: ${price:.2f} | Updated at {time.strftime('%H:%M:%S')}")
        else:
            print("Failed to fetch data. Retrying...")
        time.sleep(interval)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    user_ticker = input("Enter stock ticker symbol (e.g., AAPL, BBAI, GOOGL, TSLA): ").upper()
    refresh_rate = input("Update interval in seconds (default 10): ")
    refresh_rate = int(refresh_rate) if refresh_rate.isdigit() else 10
    track_stock(user_ticker, refresh_rate)
