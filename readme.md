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

