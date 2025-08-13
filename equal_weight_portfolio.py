import data_fetch

total_invested = 10000
total_per_tick = 10000 / len(data_fetch.tickers)
closing_by_ticker = data_fetch.fetch_closing_data()

def calc_shares(tick):
	shares = total_per_tick / tick[0]
	return shares

def get_share_amounts():
	share_amounts = []
	for i in closing_by_ticker:
		share_amounts.append(calc_shares(i))
	return share_amounts

def get_weights():
	optimal_weights = []
	for i in range(len(closing_by_ticker)):
		optimal_weights.append(1 / len(closing_by_ticker))
	return optimal_weights
portfolio = get_share_amounts()
optimal_weights = get_weights()

def get_ewp():
	return optimal_weights