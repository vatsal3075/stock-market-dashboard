# Indian Stock Market Dashboard

Interactive dashboard to analyse Nifty 50 stocks: returns, volatility,
Sharpe ratio, correlation and moving averages.

**Live demo:** https://indian-stock-market-dashboard.streamlit.app/

## Features
- Select stocks and time period (6 months to 5 years)
- KPI cards: best Sharpe, most volatile, most stable, best return
- Volatility and Sharpe ratio comparison charts
- Correlation heatmap of daily returns
- Price trend with 50 and 200 day moving averages

## Tech Stack
Python, Pandas, Plotly, Streamlit, yfinance

## Key Insights
## Key Insights
*Snapshot as of November 2026. Numbers change as live market data updates.*

- **Same-sector stocks move together:** over 1 year, TCS and INFY had a daily-return correlation of 0.78, while INFY and SBIN were almost uncorrelated (0.01). Mixing sectors gives better diversification.
- **Low volatility does not mean good returns:** ITC was the most stable stock over 1 year, yet it had the worst Sharpe ratio (-1.53).
- **SBIN stood out on risk-adjusted return:** it was the only stock with a positive Sharpe ratio over 1 year (0.45), and it also had the highest Sharpe over 3 years.
- **IT stocks were the most volatile:** INFY had the highest daily volatility over 1 year (about 2.0%), followed by TCS.
- **Results depend on the time window:** RELIANCE had a negative Sharpe ratio over 1 year but a slightly positive one over 3 years.

*Educational analysis only, not investment advice.*