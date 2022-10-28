from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dags_main.oura_dag.oura_transforms import main
from util.constants import default_args, schedule

with DAG(
    "oura",
    schedule_interval=schedule.daily_5pm_UTC.value,
    default_args=default_args,
    catchup=False,
) as dag:

    pull_oura = PythonOperator(
        task_id="pull_oura",
        python_callable=main,
    )

    pull_oura
