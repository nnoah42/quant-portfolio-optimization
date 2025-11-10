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

### 1. Equal Weight Portfolio (EWP)
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

\[
\sum_i w_i = 1, \quad w_i \ge 0
\]

## How to use

Run the main script (`main.py`) to perform the optimization and simulation, then view the summarized performance metrics.

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

