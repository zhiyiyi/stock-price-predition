import os
import duckdb
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from extract_stock_data import refresh_data
from motherduck_token import motherduck_token 

# Check if the token object is set
if token is None:
    raise ValueError("Motherduck token not found. Make sure it is set in the environment.")

if __name__ == "__main__":
    refresh_data(token)
