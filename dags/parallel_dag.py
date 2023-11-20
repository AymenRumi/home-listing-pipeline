import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from utils.logging import logger

default_args = {
    "start_date": datetime(2019, 1, 1),
    "owner": "Airflow",
    "email": "owner@test.com",
}


def process(p1):
    print("HELLO I AM TESTING THE LOGS FOR THIS PROCESSS BLAH BLAH BLAH BLAH")
    logger.task("HELLO I AM TESTING THE LOGS FOR THIS PROCESSS BLAH BLAH BLAH BLAH")
    current_directory = os.getcwd()
    print("Current Working Directory:", current_directory)

    try:
        os.makedirs("/usr/local/airflow/dags/test")
    except:
        pass
    print(p1)
    return "done"


with DAG(
    dag_id="parallel_dag",
    schedule_interval="0 0 * * *",
    default_args=default_args,
    catchup=False,
) as dag:

    # Tasks dynamically generated
    tasks = [
        BashOperator(task_id="task_{0}".format(t), bash_command="sleep 5".format(t))
        for t in range(1, 4)
    ]

    task_4 = PythonOperator(
        task_id="task_4", python_callable=process, op_args=["my super parameter"]
    )

    task_5 = BashOperator(task_id="task_5", bash_command='echo "pipeline done"')

    tasks >> task_4 >> task_5
