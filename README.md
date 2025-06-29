# Quant Portfolio Optimization

This project implements portfolio optimization by constructing and comparing four portfolio strategies:  
- Inverse Volatility  
- Risk Parity  
- Equal Weight  
- Global Minimum Variance  

Using historical returns from the following ETFs:  
**SPY**, **EFA**, **EEM**, **BND**, **VNQ**, and **TLT**.

The project runs Monte Carlo simulations to model potential future returns and calculates key performance metrics for each portfolio:  
- Mean Return  
- Sharpe Ratio  
- Volatility  

This allows evaluation and comparison of portfolio strategies under simulated market conditions.

## Portfolio Strategy Formulas

1. Equal Weight Portfolio (EWP)  
   Each asset has equal weight:  
   w_i = 1 / N

2. Global Minimum Variance Portfolio (GMVP)  
   Minimize wᵀ Σ w subject to Σ w_i = 1 and w_i ≥ 0

3. Inverse Volatility Portfolio (IVP)  
   Weights proportional to inverse volatility:  
   w_i = (1 / σ_i) / Σ_{j=1}^N (1 / σ_j)

4. Risk Parity Portfolio (RPP)  
   Minimize squared differences of risk contributions:  
   min Σ (w_i (Σ w)_i - (1/N) wᵀ Σ w)^2  
   subject to Σ w_i = 1, w_i ≥ 0

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

