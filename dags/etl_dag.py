from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

# ✅ Import functions (NO dags. prefix)
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


# 🔴 Failure callback
def on_failure_callback(context):
    logging.error(f"Task failed: {context['task_instance_key_str']}")


# ⚙️ Default arguments
default_args = {
    'owner': 'sunakshi',
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
    'on_failure_callback': on_failure_callback
}


# 🚀 DAG Definition
with DAG(
    dag_id='api_etl_pipeline_v3',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    # 🟢 Extract Task (writes extracted.csv)
    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )

    # 🟡 Transform Task (reads extracted.csv → writes transformed.csv)
    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_data
    )

    # 🔵 Load Task (reads transformed.csv → loads to DB)
    t3 = PythonOperator(
        task_id='load',
        python_callable=load_data
    )

    # 🔗 Pipeline flow
    t1 >> t2 >> t3