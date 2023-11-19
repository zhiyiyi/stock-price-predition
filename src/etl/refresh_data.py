import os
import duckdb
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from extract_stock_data import refresh_data
from os import environ
from dotenv import load_dotenv

# token = environ.get("motherduck_token", None)

# # get MotherDuck token from env
# load_dotenv(".env")
# token = os.getenv("motherduck_token")
# print(f"token: '{token}'")

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uIjoicnVpei5yaXZlcmE5My5nbWFpbC5jb20iLCJlbWFpbCI6InJ1aXoucml2ZXJhOTNAZ21haWwuY29tIiwidXNlcklkIjoiZGJiMmE2ZmYtMmZjNi00YjM2LTkzOGQtYzBmMzI5MWRlMWY4IiwiaWF0IjoxNjk5MTU2ODY3LCJleHAiOjE3MzA3MTQ0Njd9.thS_zI3creCQvb5ctSXaxt9nUvNvep7La2M-faJ0j3A"

if __name__ == "__main__":
    refresh_data(motherduck_token)