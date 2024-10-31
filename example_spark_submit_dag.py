from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

# Definisci il DAG
default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="example_spark_submit_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # Task per inviare lo script PySpark al master Spark
    spark_submit_task = SparkSubmitOperator(
        task_id="submit_spark_job",
        application="/opt/bitnami/spark/dags/example_spark_job.py",  # Percorso allo script PySpark
        conn_id="spark_default", 
        deploy_mode="client",
        executor_memory="1g",
        executor_cores=1,
        num_executors=1,
        name="example_spark_job",
        verbose=True
    )

    # Imposta la sequenza dei task nel DAG
    spark_submit_task
