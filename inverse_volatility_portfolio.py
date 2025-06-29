import data_fetch
import pandas as pd

total_invested = 10000

def compute_returns(prices):
	returns = []
	for tick_price in prices:
		tick_price_series = pd.Series(tick_price)
		curr_return = tick_price_series.pct_change().dropna()
		returns.append(curr_return)
	return returns

def calc_inverse_volatility(return_list):
	inv_volatilities = []
	for re in return_list:
		volatility = re.std()
		inv_volatility = 1 / volatility
		inv_volatilities.append(inv_volatility)
	norm_volatilities = inv_volatilities / sum(inv_volatilities)
	return norm_volatilities

def calc_shares(norm_inv_volatilities):
	amount_per = norm_inv_volatilities * total_invested
	share_amounts = []
	closing_by_ticker = data_fetch.fetch_closing_data()
	for i in range(len(norm_inv_volatilities)):
		shares = amount_per[i] / closing_by_ticker[i][0]
		share_amounts.append(shares)
	return share_amounts

returns = compute_returns(data_fetch.fetch_closing_data())
norm_inv_volatilities = calc_inverse_volatility(returns)
optimal_weights = norm_inv_volatilities
portfolio_with_numpy_vals = calc_shares(norm_inv_volatilities)
portfolio = [float(num) for num in portfolio_with_numpy_vals]

def get_ivp():
	return optimal_weights