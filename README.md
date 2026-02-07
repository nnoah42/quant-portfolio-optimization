# Quant Portfolio Optimization

This project implements portfolio optimization by constructing and comparing four portfolio strategies:  
- Inverse Volatility  
- Risk Parity  
- Equal Weight  
- Global Minimum Variance  

Using user-inputted tickers.

The project runs Monte Carlo simulations to model potential future returns and calculates key performance metrics for each portfolio:  
- Mean Return  
- Sharpe Ratio  
- Volatility  

This allows evaluation and comparison of portfolio strategies under simulated market conditions.

## Portfolio Strategy Formulas

1. Equal Weight Portfolio (EWP)
Each asset has equal weight:

\[
w_i = \frac{1}{N}
\]

---

### 2. Global Minimum Variance Portfolio (GMVP)
Minimize portfolio variance:

\[
\min_{w} \; w^\top \Sigma w
\]

Subject to:

\[
\sum_i w_i = 1, \quad w_i \ge 0
\]

---

### 3. Inverse Volatility Portfolio (IVP)
Weights proportional to inverse volatility:

\[
w_i = \frac{\frac{1}{\sigma_i}}{\sum_{j=1}^{N} \frac{1}{\sigma_j}}
\]

---

### 4. Risk Parity Portfolio (RPP)
Minimize squared differences of risk contributions:

\[
\min_w \sum_i \left( w_i (\Sigma w)_i - \frac{1}{N} w^\top \Sigma w \right)^2
\]

Subject to:
$$
\[
\sum_i w_i = 1, \quad w_i \ge 0
\]
$$

## How to use

Run the main script with tickers, date range, and an optional seed for reproducible simulations:

```bash
python main.py --tickers AAPL MSFT GOOG --start 2014-01-01 --end 2019-01-01 --seed 42
```

Skip plotting if you only want the summary:

```bash
python main.py --tickers AAPL MSFT GOOG --seed 42 --no-plot
```

Save the plot image to a file:

```bash
python main.py --tickers AAPL MSFT GOOG --seed 42 --save-plot results/monte_carlo.png
```

## Dependencies

This project requires the following Python packages (see `requirements.txt` for full list):  
- numpy  
- pandas  
- matplotlib  
- cvxpy  
- scipy  
- yfinance  

Install dependencies using:  
```bash
pip install -r requirements.txt
```

## Tests

Run the tests with:

```bash
pytest
```

## Sample Output

Example (seeded) summary output:

```text
 Inverse Volatility
------------------------------
Weights:       [0.42 0.33 0.25]
Mean Return:   0.08%
Volatility:    1.45%
Sharpe Ratio:  0.06
AAPL: 0.4200
MSFT: 0.3300
GOOG: 0.2500
```

Notes:
- Output values depend on tickers, date range, and random seed.
- Use `--seed` for reproducible simulations.

## Results (Example)

Below is a short example of how you might summarize the four strategies side‑by‑side for a given ticker set and date range:

| Strategy | Mean Return | Volatility | Sharpe |
| --- | --- | --- | --- |
| Inverse Volatility | 0.08% | 1.45% | 0.06 |
| Risk Parity | 0.07% | 1.38% | 0.05 |
| Equal Weight | 0.06% | 1.50% | 0.04 |
| Global Minimum Variance | 0.05% | 1.30% | 0.04 |

Plot output can be saved with `--save-plot` and included here:

```text
results/monte_carlo.png
```


