import numpy as np
import pandas as pd

import equal_weight_portfolio
import global_minimum_variance_portfolio
import inverse_volatility_portfolio
import risk_parity_portfolio

portfolios = ["Inverse Volatility", "Risk Parity", "Equal Weight", "Global Minimum Variance"]
final_results = []
all_paths = []
all_weights = []
tickers = []
days = 240
simulations = 250
initial_value = 10000


def compute_returns(prices):
	returns = []
	for tick_price in prices:
		tick_price_series = pd.Series(tick_price)
		curr_return = tick_price_series.pct_change().dropna()
		returns.append(curr_return)
	returns = pd.DataFrame(returns).T
	return returns

def run_sim(
	closing_by_ticker,
	tickers_list=None,
	seed=None,
	days_override=None,
	simulations_override=None,
	initial_value_override=None,
	verbose=False,
):
	global inv_vol_final, risk_parity_final, equal_weight_final, global_min_var_final
	global final_results, all_paths, all_weights, tickers

	if seed is not None:
		np.random.seed(seed)

	days_local = days_override if days_override is not None else days
	simulations_local = simulations_override if simulations_override is not None else simulations
	initial_value_local = initial_value_override if initial_value_override is not None else initial_value

	optimal_weights = [
		inverse_volatility_portfolio.get_ivp(closing_by_ticker),
		risk_parity_portfolio.get_rpp(closing_by_ticker),
		equal_weight_portfolio.get_ewp(closing_by_ticker),
		global_minimum_variance_portfolio.get_gmvp(closing_by_ticker),
	]
	all_weights = optimal_weights
	tickers = list(tickers_list) if tickers_list is not None else [f"Asset {i+1}" for i in range(len(closing_by_ticker))]
	returns = compute_returns(closing_by_ticker)
	mean_returns = returns.mean().values
	cov_matrix = returns.cov().values

	final_results = []
	all_paths = []

	for optimal_weight in optimal_weights:
		if verbose:
			for i, weight in enumerate(optimal_weight):
				print(f"{tickers[i]}: {weight}")
		results = []
		paths = []
		n = 0
		while n < simulations_local:
			simulated_returns = np.random.multivariate_normal(mean_returns, cov_matrix, days_local)
			cumulative_returns = (1 + simulated_returns).cumprod(axis=0)
			portfolio_path = cumulative_returns @ optimal_weight
			final_value = initial_value_local * portfolio_path[-1]
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

	return all_paths
