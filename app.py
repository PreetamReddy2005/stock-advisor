import yfinance as yf
import streamlit as st

st.set_page_config(page_title="Indian Stock Advisor", layout="centered")

st.title("📊 Indian Stock Advisor")
st.write("Get quick insights on popular NSE stocks.")

tickers = {
    "Infosys": "INFY.NS",
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "HDFC Bank": "HDFCBANK.NS"
}

selected = st.multiselect("Choose stocks to analyze:", list(tickers.keys()), default=["Infosys", "Reliance"])

def get_summary(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo", interval="1d")
    
    if hist.empty:
        return "⚠️ No data available."
    
    latest = hist["Close"].iloc[-1]  # Using .iloc[] for position-based access
    change = ((latest - hist["Close"].iloc[0]) / hist["Close"].iloc[0]) * 100  # Same fix here
    avg7 = hist["Close"].iloc[-7:].mean()  # Same fix here
    
    return (
        f"**Latest Price:** ₹{latest:.2f}\n"
        f"**1-Month Change:** {change:.2f}%\n"
        f"**7-Day Avg:** ₹{avg7:.2f}\n"
        f"**Volume (Last Day):** {int(hist['Volume'].iloc[-1])}"  # Fixing volume access
    )

if selected:
    for name in selected:
        st.subheader(f"📈 {name}")
        st.markdown(get_summary(tickers[name]))
