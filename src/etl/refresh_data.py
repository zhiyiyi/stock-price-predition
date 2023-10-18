import os
import duckdb
import pandas as pd
from extract_stock_data import refresh_data
from dotenv import load_dotenv


# def refresh_data(token, ticker):
#     """
#     This function refreshes the MotherDuck cloud database by extracting stock prices at 2 min intervals from our latest entry 
#     to the datetime value of when this function was activated.

#     Parameters
#     ----------
#     token: str
#         The token for connecting to the MotherDuck cloud instance.
#     ticker: str
#         The ticker symbol for the stock you want to pull data from
#     """

#     con = duckdb.connect(f"md:?motherduck_token={token}") 
#     recent_day_query = """
#     SELECT datetime
#     FROM stocks_clouddb.msft_data
#     ORDER BY datetime DESC
#     LIMIT 1
#     """

#     latest_day = con.sql(recent_day_query).fetchall()[0][0]
#     today = datetime.today()
#     # ticker = "MSFT"

#     # Extracting the historical market data (i.e. latest_day = (latest_day - timedelta(days=5)))
#     ticker = yf.Ticker(ticker)
    
#     recent_data = ticker.history(period="1d", interval="2m", start=latest_day, end=today)
#     recent_data = recent_data.rename_axis(["DateTime"]).reset_index().rename(columns={
#             "DateTime": "datetime",
#             "Open": "open_price",
#             "High": "day_high",
#             "Low": "day_low",
#             "Close": "close_price",
#             "Volume": "volume",
#             "Dividends": "dividends",
#             "Stock Splits": "stock_splits"
#         })
    
#     con.sql("INSERT INTO stocks_clouddb.msft_data SELECT * FROM recent_data")
#     con.commit()
#     con.close() 

ticker = "MSFT"
load_dotenv()
token = os.getenv("motherduck_token")


if __name__ == "__main__":
    refresh_data(token, ticker)