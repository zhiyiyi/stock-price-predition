import os
import duckdb
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from extract_stock_data import refresh_data
# from dotenv import load_dotenv
from os import environ


token = environ.get("TOKEN", None)
ticker = "MSFT"
# load_dotenv(".env")
# token = os.getenv("motherduck_token")

if __name__ == "__main__":
    refresh_data(token, ticker)