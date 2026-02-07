import monte_carlo_sim as mcs


def test_simulation_shapes():
	closing = [
		[100, 101, 102, 103, 104],
		[50, 51, 49, 52, 53],
		[200, 198, 202, 205, 207],
	]
	paths = mcs.run_sim(
		closing,
		tickers_list=["A", "B", "C"],
		seed=42,
		days_override=10,
		simulations_override=5,
		initial_value_override=1000,
	)
	assert len(paths) == 4
	assert len(paths[0]) == 5
	assert len(paths[0][0]) == 10
