TOTAL_INVESTED = 10000


def calc_shares(weights, closing_by_ticker, total_invested=TOTAL_INVESTED):
	amount_per = [weight * total_invested for weight in weights]
	share_amounts = []
	for i in range(len(closing_by_ticker)):
		shares = amount_per[i] / closing_by_ticker[i][-1]
		share_amounts.append(shares)
	return share_amounts


def get_ewp(closing_by_ticker):
	n = len(closing_by_ticker)
	return [1 / n for _ in range(n)]
