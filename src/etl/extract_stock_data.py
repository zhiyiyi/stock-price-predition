import duckdb
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta


def extract_stock_data(symbol=str):
    """
    This function extracts as much stock market data possible through the `yfinance` Python library published by Yahoo Finance.

    Parameters
    ----------
    symbol: str
        The ticker symbol for the stock you want to pull data from
    """

    # The yfinance API allows you to retrieve 2 years worth of data on a per-hour basis
    # So the code below will allow us to get exactly that amount from today's date
    today = datetime.today()
    date = today - timedelta(days=729)

    # Extracting the historical market data
    ticker = yf.Ticker(symbol)
    hist_2yr = ticker.history(
        period="1d", interval="1h", start=date, end=today)

    # Extracting stock data on a per-day basis from the time of it's initial listing to our `date` object
    init_hist = ticker.history(period="max", interval="1d", end=date)

    # Combining the two DatFrames to generate a df of stock data for a given stock ticker
    stock_df = pd.concat([init_hist, hist_2yr])

    # Assigning our timestamp index with its own column then resetting the index.
    stock_df = stock_df.rename_axis(["DateTime"]).reset_index().rename(columns={
        "DateTime": "datetime",
        "Open": "open_price",
        "High": "day_high",
        "Low": "day_low",
        "Close": "close_price",
        "Volume": "volume",
        "Dividends": "dividends",
        "Stock Splits": "stock_splits"
    })

    return stock_df


def refresh_data(token):
    """
    This function refreshes the MotherDuck cloud database by extracting stock prices at 2 min intervals from our latest entry 
    to the datetime value of when this function was activated.

    Parameters
    ----------
    token: str
        The token for connecting to the MotherDuck cloud instance.
    ticker: str
        The ticker symbol for the stock you want to pull data from
    """

    try:
        con = duckdb.connect(f"md:?motherduck_token={token}")
        recent_day_query = """
        SELECT datetime
        FROM stocks_clouddb.msft_data
        ORDER BY datetime DESC
        LIMIT 1
        """

        latest_day = con.sql(recent_day_query).fetchall()[0][0]
        today = datetime.today()
        ticker = "MSFT"

        # Extracting the historical market data (i.e. latest_day = (latest_day - timedelta(days=5)))
        ticker = yf.Ticker(ticker)

        recent_data = ticker.history(
            period="1d", interval="2m", start=latest_day, end=today)
        recent_data = recent_data.rename_axis(["DateTime"]).reset_index().rename(columns={
            "DateTime": "datetime",
            "Open": "open_price",
            "High": "day_high",
            "Low": "day_low",
            "Close": "close_price",
            "Volume": "volume",
            "Dividends": "dividends",
            "Stock Splits": "stock_splits"
        })

        con.sql("INSERT INTO stocks_clouddb.msft_data SELECT * FROM recent_data")
        con.commit()
        con.close()
    
    except duckdb.duckdb.BinderException as e:
        if "table msft_data has 8 columns but 7 values were supplied" in str(e):
            print("The most recent stock data has already been extracted. Refreshing the database is not necessary.")
        else:
            # Handle other BinderExceptions or re-raise the exception
            raise