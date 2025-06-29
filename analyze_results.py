import monte_carlo_sim
import pandas as pd

i = 0
for method in monte_carlo_sim.final_results:
	print(f"{monte_carlo_sim.portfolios[i]}: ")
	result = pd.DataFrame(method).T
	result.columns = monte_carlo_sim.portfolios[i]
	print(result.describe())

result = pd.DataFrame(monte_carlo_sim.final_results).T
result.columns = monte_carlo_sim.portfolios[i]
print(result.describe())
