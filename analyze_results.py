import pandas as pd

import monte_carlo_sim


def analyze_results(closing_by_ticker, tickers_list=None, seed=None):
	monte_carlo_sim.run_sim(closing_by_ticker, tickers_list=tickers_list, seed=seed)
	i = 0
	for method in monte_carlo_sim.final_results:
		print(f"{monte_carlo_sim.portfolios[i]}: ")
		result = pd.DataFrame(method).T
		result.columns = monte_carlo_sim.portfolios[i]
		print(result.describe())
		i += 1

	result = pd.DataFrame(monte_carlo_sim.final_results).T
	result.columns = monte_carlo_sim.portfolios
	print(result.describe())


if __name__ == "__main__":
	raise SystemExit("Run via main.py")
