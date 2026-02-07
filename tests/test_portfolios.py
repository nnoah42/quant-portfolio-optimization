import numpy as np

import equal_weight_portfolio as ewp
import global_minimum_variance_portfolio as gmvp
import inverse_volatility_portfolio as ivp
import risk_parity_portfolio as rpp


def _sample_closing_data():
	return [
		[100, 101, 102, 103, 104],
		[50, 51, 49, 52, 53],
		[200, 198, 202, 205, 207],
	]


def _assert_weights(weights):
	assert np.isclose(sum(weights), 1.0)
	assert all(w >= 0 for w in weights)


def test_equal_weight():
	weights = ewp.get_ewp(_sample_closing_data())
	_assert_weights(weights)


def test_inverse_volatility():
	weights = ivp.get_ivp(_sample_closing_data())
	_assert_weights(weights)


def test_risk_parity():
	weights = rpp.get_rpp(_sample_closing_data())
	_assert_weights(weights)


def test_global_min_variance():
	weights = gmvp.get_gmvp(_sample_closing_data())
	_assert_weights(weights)
