import inverse_volatility_portfolio
import risk_parity_portfolio
import equal_weight_portfolio
import global_minimum_variance_portfolio
import data_fetch
import pandas as pd
import numpy as np

portfolios = ["Inverse Volatility", "Risk Parity", "Equal Weight", "Global Minumum Variance"]
optimal_weights = [inverse_volatility_portfolio.optimal_weights, risk_parity_portfolio.optimal_weights, equal_weight_portfolio.optimal_weights, global_minimum_variance_portfolio.optimal_weights]

def compute_returns(prices):
	returns = []
	for tick_price in prices:
		tick_price_series = pd.Series(tick_price)
		curr_return = tick_price_series.pct_change().dropna()
		returns.append(curr_return)
	returns = pd.DataFrame(returns).T
	return returns

closing_by_ticker = data_fetch.fetch_closing_data()
returns = compute_returns(closing_by_ticker)
mean_returns = returns.mean().values
cov_matrix = returns.cov().values

days = 240
simulations = 250
initial_value = 10000

final_results = []
all_paths = []

for optimal_weight in optimal_weights:
	results = []
	paths = []
	n = 0
	while n < simulations:
		simulated_returns = np.random.multivariate_normal(mean_returns,cov_matrix,days)
		cumulative_returns = (1 + simulated_returns).cumprod(axis=0)
		portfolio_path = cumulative_returns @ optimal_weight
		final_value = initial_value * portfolio_path[-1]
		results.append(final_value)
		n += 1
		results = [float(k) for k in results]

		paths.append(portfolio_path)
		
	
	final_results.append(results)
	all_paths.append(paths)

inv_vol_final = all_paths[0]
risk_parity_final = all_paths[1]
equal_weight_final = all_paths[2]
global_min_var_final = all_paths[3]

def get_paths():
	return all_paths