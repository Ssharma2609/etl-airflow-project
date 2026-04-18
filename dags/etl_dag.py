from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import logging

# ✅ Import modular functions
from extract import extract_data
from transform import transform_data
from load import load_data


# 🔴 Failure callback
def on_failure_callback(context):
    logging.error(f"Task failed: {context['task_instance_key_str']}")


# 🟢 Extract Task
def extract_task(**context):
    df = extract_data()
    context['ti'].xcom_push(key='data', value=df.to_json())


# 🟡 Transform Task
def transform_task(**context):
    data = context['ti'].xcom_pull(key='data')
    df = pd.read_json(data)

    df = transform_data(df)

    context['ti'].xcom_push(key='data', value=df.to_json())


# 🔵 Load Task
def load_task(**context):
    data = context['ti'].xcom_pull(key='data')
    df = pd.read_json(data)

    load_data(df)


# ⚙️ Default arguments
default_args = {
    'owner': 'sunakshi',
    'start_date': datetime(2024, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
    'on_failure_callback': on_failure_callback
}


# 🚀 DAG Definition
with DAG(
    dag_id='api_etl_pipeline_v3',   # ✅ NEW DAG NAME
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract_task
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_task
    )

    t3 = PythonOperator(
        task_id='load',
        python_callable=load_task
    )

    # 🔗 Pipeline order
    t1 >> t2 >> t3