import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Indian Stock Dashboard", page_icon="📈", layout="wide")

st.title("📈 Indian Stock Market Dashboard")
st.caption("Educational analysis only, not investment advice.")

all_stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ITC.NS", "SBIN.NS", "WIPRO.NS"]

selected = st.sidebar.multiselect("Select stocks", all_stocks, default=all_stocks)
period = st.sidebar.selectbox("Time period", ["6mo", "1y", "3y", "5y"], index=1)

if not selected:
    st.warning("Please select at least one stock.")
    st.stop()

@st.cache_data
def get_data(stock, period):
    return yf.download(stock, period=period)

risk_free = 0.065
results = []
returns_df = pd.DataFrame()

for stock in selected:
    df = get_data(stock, period)
    returns = df["Close"][stock].pct_change()
    returns_df[stock] = returns
    results.append({
        "Stock": stock,
        "Avg Return": returns.mean(),
        "Volatility": returns.std(),
        "Sharpe": round(((returns.mean() - risk_free / 252) / returns.std()) * (252 ** 0.5), 2)
    })

table = pd.DataFrame(results)

# ---------- KPI cards ----------
best_sharpe = table.loc[table["Sharpe"].idxmax()]
most_vol = table.loc[table["Volatility"].idxmax()]
least_vol = table.loc[table["Volatility"].idxmin()]
best_ret = table.loc[table["Avg Return"].idxmax()]

k1, k2, k3, k4 = st.columns(4)
k1.metric("Best Sharpe", best_sharpe["Stock"], f"{best_sharpe['Sharpe']}", delta_color="off")
k2.metric("Most Volatile", most_vol["Stock"], f"{most_vol['Volatility']:.4f}", delta_color="off")
k3.metric("Most Stable", least_vol["Stock"], f"{least_vol['Volatility']:.4f}", delta_color="off")
k4.metric("Best Avg Return", best_ret["Stock"], f"{best_ret['Avg Return']:.5f}", delta_color="off")

st.divider()

# ---------- Row 1: Volatility | Sharpe ----------
c1, c2 = st.columns(2)

with c1:
    fig1 = px.bar(table, x="Stock", y="Volatility", title=f"Volatility ({period})", height=380)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    fig2 = px.bar(table, x="Stock", y="Sharpe", color="Sharpe",
                  color_continuous_scale="RdYlGn", title=f"Sharpe Ratio ({period})", height=380)
    st.plotly_chart(fig2, use_container_width=True)

# ---------- Row 2: Heatmap | Price trend ----------
c3, c4 = st.columns(2)

with c3:
    corr = returns_df.corr()
    fig3 = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                     zmin=-1, zmax=1, title=f"Correlation ({period})", height=420)
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    chosen = st.selectbox("Stock for price trend", selected)
    price = get_data(chosen, period)["Close"][chosen]
    chart_df = pd.DataFrame({
        "Price": price,
        "50 DMA": price.rolling(50).mean(),
        "200 DMA": price.rolling(200).mean()
    })
    st.line_chart(chart_df, height=340)

# ---------- Table ----------
with st.expander("📋 View data table"):
    st.dataframe(table, use_container_width=True)