import numpy as np

import monte_carlo_sim

def _calc_return_stats(portfolio_paths):
    # portfolio_paths shape: (simulations, days)
    returns = portfolio_paths[:, 1:] / portfolio_paths[:, :-1] - 1
    avg_return = np.mean(returns)
    volatility = np.std(returns)
    sharpe_ratio = avg_return / volatility if volatility != 0 else 0.0
    return avg_return, volatility, sharpe_ratio


def summarize_results(closing_by_ticker, tickers_list=None, seed=None):
    monte_carlo_sim.run_sim(closing_by_ticker, tickers_list=tickers_list, seed=seed, verbose=False)
    paths = np.array(monte_carlo_sim.all_paths)

    iv_mean_sharpe = _calc_return_stats(paths[0])
    rp_mean_sharpe = _calc_return_stats(paths[1])
    ew_mean_sharpe = _calc_return_stats(paths[2])
    gmv_mean_sharpe = _calc_return_stats(paths[3])

    iv_summary_stats = {
        "label": "Inverse Volatility",
        "weights": monte_carlo_sim.all_weights[0],
        "mean_return": iv_mean_sharpe[0],
        "volatility": iv_mean_sharpe[1],
        "sharpe_ratio": iv_mean_sharpe[2]
    }

    rp_summary_stats = {
        "label": "Risk Parity",
        "weights": monte_carlo_sim.all_weights[1],
        "mean_return": rp_mean_sharpe[0],
        "volatility": rp_mean_sharpe[1],
        "sharpe_ratio": rp_mean_sharpe[2]
    }

    ew_summary_stats = {
        "label": "Equal Weight",
        "weights": monte_carlo_sim.all_weights[2],
        "mean_return": ew_mean_sharpe[0],
        "volatility": ew_mean_sharpe[1],
        "sharpe_ratio": ew_mean_sharpe[2]
    }

    gmv_summary_stats = {
        "label": "Global Minimum Variance",
        "weights": monte_carlo_sim.all_weights[3],
        "mean_return": gmv_mean_sharpe[0],
        "volatility": gmv_mean_sharpe[1],
        "sharpe_ratio": gmv_mean_sharpe[2]
    }

    rows = [
        iv_summary_stats,
        rp_summary_stats,
        ew_summary_stats,
        gmv_summary_stats,
    ]

    ticker_headers = monte_carlo_sim.tickers
    headers = ["Strategy", "Mean", "Vol", "Sharpe"] + ticker_headers

    table_rows = []
    for stats in rows:
        row = [
            stats["label"],
            f"{stats['mean_return']:.2%}",
            f"{stats['volatility']:.2%}",
            f"{stats['sharpe_ratio']:.2f}",
        ]
        for i in range(len(ticker_headers)):
            row.append(f"{stats['weights'][i]:.3f}")
        table_rows.append(row)

    col_widths = [
        max(len(headers[i]), max(len(r[i]) for r in table_rows))
        for i in range(len(headers))
    ]

    def format_row(values):
        return "  ".join(values[i].ljust(col_widths[i]) for i in range(len(values)))

    print(format_row(headers))
    print("  ".join("-" * w for w in col_widths))
    for row in table_rows:
        print(format_row(row))

if __name__ == "__main__":
    raise SystemExit("Run via main.py")
