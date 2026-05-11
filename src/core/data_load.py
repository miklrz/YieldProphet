import yfinance as yf
import pandas as pd


def fetch_data(ticker: str) -> pd.DataFrame:
    """Загрузка данных из Yahoo Finance."""
    data = yf.download(ticker, period="5y")

    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    df_prophet = data[["Close"]].reset_index()
    df_prophet.columns = ["ds", "y"]

    df_prophet["ds"] = df_prophet["ds"].dt.tz_localize(None)
    return df_prophet
