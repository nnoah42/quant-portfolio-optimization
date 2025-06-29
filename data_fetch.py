import yfinance as yf
tickers_qpo = ["SPY","EFA","EEM","BND","VNQ","TLT"]
start_date = "2014-01-01"
end_date = "2019-01-01"

def fetch_closing_data():
	data = yf.download(tickers_qpo,start=start_date,end=end_date,progress=False)
	spy_close = data["Close"]["SPY"].tolist()
	efa_close = data["Close"]["EFA"].tolist()
	eem_close = data["Close"]["EEM"].tolist()
	bnd_close = data["Close"]["BND"].tolist()
	vnq_close = data["Close"]["VNQ"].tolist()
	tlt_close = data["Close"]["TLT"].tolist()
	closing_by_ticker = [spy_close,efa_close,eem_close,bnd_close,vnq_close,tlt_close]
	return closing_by_ticker

