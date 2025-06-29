import monte_carlo_sim
import numpy as np

def summarize_results():
    paths = np.array(monte_carlo_sim.get_paths())
    portfolios = ["Inverse Volatility", "Risk Parity", "Equal Weight", "Global Minumum Variance"]

    def calc_sharpe(portfolio_paths):
        rf = 0
        volatility = np.std(portfolio_paths)
        avg_return = np.mean(portfolio_paths[:,-1]) - 1
        sharpe_ratio = (avg_return - rf) / volatility
        return avg_return, volatility, sharpe_ratio

    iv_mean_sharpe = calc_sharpe(paths[0])
    rp_mean_sharpe = calc_sharpe(paths[1])
    ew_mean_sharpe = calc_sharpe(paths[2])
    gmv_mean_sharpe = calc_sharpe(paths[3])

    iv_summary_stats = {
        "label": "Inverse Volatility",
        "mean_return": iv_mean_sharpe[0],
        "volatility": iv_mean_sharpe[1],
        "sharpe_ratio": iv_mean_sharpe[2]
    }

    rp_summary_stats = {
        "label": "Risk Parity",
        "mean_return": rp_mean_sharpe[0],
        "volatility": rp_mean_sharpe[1],
        "sharpe_ratio": rp_mean_sharpe[2]
    }

    ew_summary_stats = {
        "label": "Equal Weight",
        "mean_return": ew_mean_sharpe[0],
        "volatility": ew_mean_sharpe[1],
        "sharpe_ratio": ew_mean_sharpe[2]
    }

    gmv_summary_stats = {
        "label": "Global Minimum Variance",
        "mean_return": gmv_mean_sharpe[0],
        "volatility": gmv_mean_sharpe[1],
        "sharpe_ratio": gmv_mean_sharpe[2]
    }

    def print_summary(stats):
        print(f"\n {stats['label']}")
        print("-" * 30)
        print(f"Mean Return:   {stats['mean_return']:.2%}")
        print(f"Volatility:    {stats['volatility']:.2%}")
        print(f"Sharpe Ratio:  {stats['sharpe_ratio']:.2f}")
        
        
    print_summary(iv_summary_stats)
    print_summary(rp_summary_stats)
    print_summary(ew_summary_stats)
    print_summary(gmv_summary_stats)