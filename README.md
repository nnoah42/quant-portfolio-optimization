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

### 1. Equal Weight Portfolio (EWP)
Each asset is assigned an equal weight:
\[
w_i = \frac{1}{N}
\]
where \(N\) is the number of assets.

---

### 2. Global Minimum Variance Portfolio (GMVP)
Minimize the portfolio variance subject to the weights summing to 1 and no short selling:
\[
\begin{aligned}
\min_{w} \quad & w^T \Sigma w \\
\text{subject to} \quad & \sum_{i=1}^N w_i = 1 \\
& w_i \geq 0, \quad i=1,\dots,N
\end{aligned}
\]
where \(\Sigma\) is the covariance matrix of asset returns.

---

### 3. Inverse Volatility Portfolio (IVP)
Weights are proportional to the inverse of each asset's volatility:
\[
w_i = \frac{\frac{1}{\sigma_i}}{\sum_{j=1}^N \frac{1}{\sigma_j}}
\]
where \(\sigma_i\) is the standard deviation (volatility) of asset \(i\).

---

### 4. Risk Parity Portfolio (RPP)
Weights are chosen such that each asset contributes equally to the total portfolio risk (volatility). This is done by minimizing the difference in risk contributions:
\[
\min_w \sum_{i=1}^N \left( w_i (\Sigma w)_i - \frac{1}{N} w^T \Sigma w \right)^2
\]
subject to:
\[
\sum_{i=1}^N w_i = 1, \quad w_i \geq 0
\]
where:
- \(w_i\) is the weight of asset \(i\)
- \(\Sigma\) is the covariance matrix
- \((\Sigma w)_i\) is the \(i^{th}\) element of the vector \(\Sigma w\) (marginal risk contribution)
- \(w^T \Sigma w\) is the total portfolio variance

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

