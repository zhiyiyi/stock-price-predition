import os
import duckdb
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from src.etl.extract_stock_data import refresh_data
from os import environ
# from dotenv import load_dotenv

token = environ.get("TOKEN", None)
print(f"token: '{token}'")
# ticker = "MSFT"
# load_dotenv(".env")
# token = os.getenv("motherduck_token")

if __name__ == "__main__":
    refresh_data(token)
