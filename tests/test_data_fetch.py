import pandas as pd

import data_fetch


def test_normalize_close_data_single_ticker():
	close = pd.Series([1.0, 2.0, 3.0], name="AAPL")
	result = data_fetch._normalize_close_data(close, ["AAPL"])
	assert result == [[1.0, 2.0, 3.0]]
