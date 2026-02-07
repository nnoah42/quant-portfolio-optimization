import numpy as np
import pandas as pd

TOTAL_INVESTED = 10000


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
	norm_volatilities = np.array(inv_volatilities) / sum(inv_volatilities)
	return norm_volatilities


def calc_shares(weights, closing_by_ticker, total_invested=TOTAL_INVESTED):
	amount_per = weights * total_invested
	share_amounts = []
	for i in range(len(weights)):
		shares = amount_per[i] / closing_by_ticker[i][-1]
		share_amounts.append(shares)
	return share_amounts


def get_ivp(closing_by_ticker):
	returns = compute_returns(closing_by_ticker)
	return calc_inverse_volatility(returns)
