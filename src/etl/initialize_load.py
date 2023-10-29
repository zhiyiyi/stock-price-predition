# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
import duckdb
from src.etl.extract_stock_data import extract_stock_data
upstream = None

# -

upstream = None


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
    CREATE TABLE IF NOT EXISTS {table_name} (
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
    # persistent table
    connection.sql(f"INSERT INTO {table_name} SELECT * FROM df")

    # Saving our progress
    connection.commit()

    # Close the connection
    connection.close()


# Executing the program
if __name__ == "__main__":
    table_name = "msft_data"
    ticker = "MSFT"
    database_name = "msft_database"

    # Extracting stock data from the yfinance API
    df = extract_stock_data(ticker)

    # Initialize DuckDB database and create a table
    initialize_duckdb(table_name, df, database_name)
