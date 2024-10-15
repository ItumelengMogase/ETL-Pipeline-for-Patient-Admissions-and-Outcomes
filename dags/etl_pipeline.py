from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 14),  # Set to the current date
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'default_dag', 
    default_args=default_args, 
    description='A default DAG for starting point',
    schedule_interval='@daily',  # Set to run daily
    catchup=False
) as dag:

    # Dummy task to indicate start of the DAG
    start_task = DummyOperator(
        task_id='start'
    )

    # Dummy task to indicate end of the DAG
    end_task = DummyOperator(
        task_id='end'
    )

    # Set task dependencies
    start_task >> end_task
