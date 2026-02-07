import argparse

import data_fetch
import plot_results as pr
import summarize_results as sr


def parse_args():
	parser = argparse.ArgumentParser(description="Quant portfolio optimization runner")
	parser.add_argument("--tickers", nargs="+", help="List of tickers, e.g., AAPL MSFT GOOG")
	parser.add_argument("--start", default=data_fetch.DEFAULT_START_DATE, help="Start date (YYYY-MM-DD)")
	parser.add_argument("--end", default=data_fetch.DEFAULT_END_DATE, help="End date (YYYY-MM-DD)")
	parser.add_argument("--seed", type=int, default=None, help="Random seed for simulations")
	parser.add_argument("--no-plot", action="store_true", help="Skip plotting the simulation paths")
	parser.add_argument("--save-plot", default=None, help="Optional path to save the plot image")
	return parser.parse_args()


def main():
	args = parse_args()
	tickers_list = args.tickers if args.tickers else data_fetch.collect_tickers()
	closing_by_ticker = data_fetch.fetch_closing_data(
		tickers_list=tickers_list,
		start_date=args.start,
		end_date=args.end,
	)

	sr.summarize_results(closing_by_ticker, tickers_list=tickers_list, seed=args.seed)
	if not args.no_plot:
		pr.plot_results(
			closing_by_ticker,
			tickers_list=tickers_list,
			seed=args.seed,
			save_path=args.save_plot,
		)


if __name__ == "__main__":
	main()
