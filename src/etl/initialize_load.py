import duckdb
import pandas as pd
import numpy as np
from extract_stock_data import extract_stock_data

def initialize_duckdb(table_name, df, db_name):
    """
    This function initialize a DuckDB database then loads our stock data to the table we generated for it.

    Parameters
    ----------
    table_name: str
        The name we're giving our table which will store our stock data.
    df: obj
        The DataFrame containing the stock data extracted from the `yfinance` API we'll be loading to our initialized DuckDB database.
    db_name: str
        The name we're giving our DuckDB database.
    """
    # Initialize a DuckDB connection
    connection = duckdb.connect(f"{db_name}.duckdb", read_only=False)

    # Create a table
    create_table_query = f"""
    CREATE TABLE {table_name} (
        datetime TIMESTAMP,
        open_price DOUBLE,
        day_high DOUBLE,
        day_low DOUBLE,
        close_price DOUBLE,
        volume INTEGER,
        dividends DOUBLE,
        stock_splits FLOAT
    );
    """    

    connection.sql(create_table_query)
    
    # Load Pandas DataFrame into the DuckDB table
    connection.sql("INSERT INTO msft_data SELECT * FROM df") #persistent table
    
    # Saving our progress
    connection.commit()

    # Close the connection
    connection.close()


# Executing the program
if __name__ == "__main__":
    
    # Specifying the names of our table and the stock ticker we want to pull data from:
    table_name = str(input("Provide a table name: "))
    ticker = str(input("Enter the ticker symbol you wish to extract data for (i.e. 'MSFT'): "))
    database_name = str(input("Provide a name for the DuckDB database we'll be creating: "))

    # Extracting stock data from the yfinance API
    df = extract_stock_data(ticker)

    # Initialize DuckDB database and create a table
    initialize_duckdb(table_name, df, database_name)