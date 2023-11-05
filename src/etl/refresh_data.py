import os
import duckdb
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from extract_stock_data import refresh_data
from os import environ
# from dotenv import load_dotenv

token = environ.get("motherduck_token", None)
# ticker = "MSFT"
# load_dotenv(".env")
# token = os.getenv("motherduck_token")

if __name__ == "__main__":
    refresh_data(token)