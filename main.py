import yfinance as yf
import pandas as pd

tickers = ["INFY.NS", "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]

def summarize_stock(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo", interval="1d")

    if hist.empty:
        return f"⚠️ No data found for {ticker}"

    latest_price = hist["Close"][-1]
    old_price = hist["Close"][0]
    change_percent = ((latest_price - old_price) / old_price) * 100
    avg_7day = hist["Close"][-7:].mean()

    summary = (
        f"📈 {ticker}\n"
        f"• Latest Price: ₹{latest_price:.2f}\n"
        f"• 1-Month Change: {change_percent:.2f}%\n"
        f"• 7-Day Avg: ₹{avg_7day:.2f}\n"
        f"• Volume (last day): {hist['Volume'][-1]}\n"
    )

    return summary

results = [summarize_stock(ticker) for ticker in tickers]
final_prompt = "\n\n".join(results)
print(final_prompt)
