from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from extract_stock_data import refresh_data


# Define default_args dictionary to specify default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'refresh_msft_data',
    default_args=default_args,
    description='Refresh MSFT data every Friday',
    schedule_interval='@weekly',
)

# Define the PythonOperator task
refresh_task = PythonOperator(
    task_id='refresh_msft_data_task',
    python_callable=refresh_data,
    dag=dag,
)

# Set task dependencies
refresh_task

if __name__ == "__main__":
    dag.cli()
