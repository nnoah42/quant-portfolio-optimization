import data_fetch
import cvxpy as cp
import pandas as pd

total_invested = 10000
closing_by_ticker = data_fetch.fetch_closing_data()

def compute_returns(prices):
	returns = []
	for tick_price in prices:
		tick_price_series = pd.Series(tick_price)
		curr_return = tick_price_series.pct_change().dropna()
		returns.append(curr_return)
	returns = pd.DataFrame(returns).T
	return returns

def compute_cov_matrix(closing):
	cov_matrix = compute_returns(closing).cov().values
	return cov_matrix

cov_matrix = compute_cov_matrix(closing_by_ticker)

def optimize():
	w = cp.Variable(len(closing_by_ticker))
	objective = cp.Minimize(cp.quad_form(w,cov_matrix))
	constraints = [cp.sum(w) == 1, w >= 0]
	problem = cp.Problem(objective,constraints)
	problem.solve()
	optimal_weights = w.value
	return optimal_weights

def calc_shares(weights):
	shares = []
	total_per = [weight * total_invested for weight in weights]
	for i in range(len(closing_by_ticker)):
		share_amount = total_per[i] / closing_by_ticker[i][0]
		shares.append(share_amount)
	return shares


optimal_weights = optimize()
optimal_weights = [max(0, w) for w in optimal_weights]
total = sum(optimal_weights)
for i in range(len(optimal_weights)):
	optimal_weights[i] = optimal_weights[i] / total

optimal_weights = [float(num) for num in optimal_weights]

portfolio = calc_shares(optimal_weights)

def get_gmvp():
	return optimal_weights