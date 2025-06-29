import pandas as pd
import data_fetch
import numpy as np
import warnings
from scipy.optimize import minimize

warnings.filterwarnings("ignore", message="YF.download() has changed argument auto_adjust")

closing_by_ticker = data_fetch.fetch_closing_data()
total_invested = 10000

def compute_returns(prices):
	returns = []
	for tick_price in prices:
		tick_price_series = pd.Series(tick_price)
		curr_return = tick_price_series.pct_change().dropna()
		returns.append(curr_return)
	returns = pd.DataFrame(returns).T
	return returns

def calc_volatility(return_list):
	volatilities = []
	for re in return_list:
		volatility = re.std()
		volatilities.append(volatility)
	return volatilities

def compute_cov_matrix(closing):
	cov_matrix = compute_returns(closing).cov().values
	return cov_matrix

def risk_contribution(weights, cov_matrix):
    portfolio_vol = np.sqrt(weights.T @ cov_matrix @ weights)
    marginal_contrib = cov_matrix @ weights / portfolio_vol
    return weights * marginal_contrib

def risk_parity_objective(weights, cov_matrix):
	rc = risk_contribution(weights, cov_matrix)
	avg_rc = np.mean(rc)
	return np.sum((rc - avg_rc) ** 2)

cov_matrix = compute_cov_matrix(closing_by_ticker)
n_assets = cov_matrix.shape[0]
initial_guess = initial_guess = np.ones(n_assets) / n_assets
bounds = [(0, 1) for i in range(n_assets)]
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

result = minimize(
    fun=risk_parity_objective,
    x0=initial_guess,
    args=(cov_matrix,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints,
    options={'ftol': 1e-12, 'maxiter': 500, 'disp': False}
)

optimal_weights = result.x
allocations = optimal_weights * total_invested

def calc_shares():
	shares = []
	for i in range(len(allocations)):
		num_shares = allocations[i] / closing_by_ticker[i][0]
		shares.append(num_shares)
	shares = [float(j) for j in shares]
	return shares

portfolio = calc_shares()

def get_rpp():
	return optimal_weights