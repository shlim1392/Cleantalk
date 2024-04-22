from airflow import DAG
from pendulum import yesterday
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
# from airflow.providers.apache.hdfs.sensors.web_hdfs import WebHdfsSensor
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor  # FileSensor 임포트 추가

import datetime  # datetime 모듈 추가

target_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

dag = DAG(
    dag_id="sql",
    schedule_interval="@daily",
    start_date=yesterday("Asia/Seoul"),
    catchup=False
)

spark_submit_task = SparkSubmitOperator(
    task_id="sqldb",
    application="/home/big/airflow/dags/sparkapp.py",
    conn_id="spark_default",
    dag=dag
)

exists = FileSensor(
    task_id="exists",
    filepath=f'/home/big/temp/sql_{target_date}.csv',
    poke_interval=30,
    dag=dag
)




