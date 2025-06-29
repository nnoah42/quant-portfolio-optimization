from matplotlib import pyplot as plt
import monte_carlo_sim

def plot_results():
    fig, axes = plt.subplots(2, 2, figsize=(12, 6))

    for i in range(monte_carlo_sim.simulations):
        axes[0][0].plot(monte_carlo_sim.inv_vol_final[i] * 10000, linewidth=0.8, alpha=0.4)
    axes[0][0].set_title('Inverse Volatility Portfolio Monte Carlo Sim')
    axes[0][0].set_xlabel('Time Step')
    axes[0][0].set_ylabel('Simulated Value')
    axes[0][0].grid(True)

    for i in range(monte_carlo_sim.simulations):
        axes[1][0].plot(monte_carlo_sim.risk_parity_final[i] * 10000, linewidth=0.8, alpha=0.4)
    axes[1][0].set_title('Risk Parity Portfolio Monte Carlo Sim')
    axes[1][0].set_xlabel('Time Step')
    axes[1][0].set_ylabel('Simulated Value')
    axes[1][0].grid(True)

    for i in range(monte_carlo_sim.simulations):
        axes[1][1].plot(monte_carlo_sim.equal_weight_final[i] * 10000, linewidth=0.8, alpha=0.4)
    axes[1][1].set_title('Equal Weight Portfolio Monte Carlo Sim')
    axes[1][1].set_xlabel('Time Step')
    axes[1][1].set_ylabel('Simulated Value')
    axes[1][1].grid(True)

    for i in range(monte_carlo_sim.simulations):
        axes[0][1].plot(monte_carlo_sim.global_min_var_final[i] * 10000, linewidth=0.8, alpha=0.4)
    axes[0][1].set_title('Global Minimum Variance Portfolio Monte Carlo Sim')
    axes[0][1].set_xlabel('Time Step')
    axes[0][1].set_ylabel('Simulated Value')
    axes[0][1].grid(True)

    plt.tight_layout()
    plt.show()