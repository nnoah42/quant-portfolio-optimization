import yfinance as yf
import warnings
warnings.filterwarnings("ignore", message="YF.download() has changed argument auto_adjust")
tickers = []
start_date = "2014-01-01"
end_date = "2019-01-01"

print("How many tickers do you want to add?")
num_tickers = int(input())
while len(tickers) < num_tickers:
    print(f"Enter ticker {len(tickers)+1}:")
    ticker = input().strip().upper()
    try:
        ticker_obj = yf.Ticker(ticker)
        info = ticker_obj.info
        current_price = info.get('regularMarketPrice')
        
        if current_price != None:
            tickers.append(ticker)
        else:
            print(f"Invalid ticker: {ticker} - No price data available")
    except:
        print(f"Invalid ticker: {ticker}")
        continue

def fetch_closing_data():
    data = yf.download(tickers,start=start_date,end=end_date,progress=False,auto_adjust=True)
    closing_by_ticker = [data["Close"][ticker].tolist() for ticker in tickers]
    return closing_by_ticker
 